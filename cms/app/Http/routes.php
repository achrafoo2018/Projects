<?php

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It's a breeze. Simply tell Laravel the URIs it should respond to
| and give it the controller to call when that URI is requested.
|
*/

Route::get('/', function () {
    return view('welcome');
});
//Route::get('/post/{id}', 'PostController@index');
/*Route::get('/admin/posts', array("as"=>"admin.home", function(){
    $url = route("admin.home");
    return "this url is ".$url;
}));*/
/*Route::resource("posts", "PostController");
Route::get('/contact/{id}', 'PostController@contact');*/
Route::get('/insert', function(){
    DB::insert('insert into posts(title, content) values(?, ?)', ['PHP with laravel', 'laravel is da best framework']);
});
Route::get('/posts/{id}', 'PostController@getPost');