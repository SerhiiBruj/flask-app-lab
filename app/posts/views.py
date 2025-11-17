from flask import render_template, current_app, request,redirect, url_for
from . import posts_bp
from .models import Post
from app import db
from .forms import PostForm
from  flask import flash 


@posts_bp.route('/post')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).limit(10).all()
    return render_template('posts.html', posts=posts)



@posts_bp.route('/post/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            category=form.category.data,
            author=form.author.data
        )
        db.session.add(post)
        db.session.commit()
        flash("Post added successfully", "success")
        return redirect(url_for('posts.index'))  # PRG
    return render_template('add_post.html', form=form)

@posts_bp.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('detail_posts.html', post=post)

@posts_bp.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if request.method == 'POST' and form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()
        flash("Post updated successfully", "success")
        return redirect(url_for('posts.index'))
  
    return render_template('add_post.html', form=form)

@posts_bp.route('/post/delete_confirm/<int:id>', methods=['GET', 'POST'])
def delete_confirm(id):
    post = Post.query.get_or_404(id)
    return render_template('confirm_delete.html', post=post)

@posts_bp.route('/post/delete/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", "danger")
        return redirect(url_for('posts.index'))
    return render_template('confirm_delete.html', post=post)
