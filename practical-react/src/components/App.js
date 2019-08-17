import React, { Component } from 'react';
import './App.css';
import constants from './constants';
class newsAPI extends Component {
  constructor(){
    super();
    this.state = {
      link : "",
      result: [],
      title:"",
      pub_date:"",
      category:"",
      cover_image:"",
      content:"",
      author:""
    };
  }
 
  handleLinkChange = ( event ) =>{
    this.setState({link: event.target.value});
  }

  handleTitleChange = ( event ) =>{
    this.setState({title: event.target.value});
  }

  handlePubDateChange = ( event ) =>{
    this.setState({pub_date: event.target.value});
  }

  handleCategoryChange = ( event ) =>{
    this.setState({category: event.target.value});
  }

  handleImageChange = ( event ) =>{
    this.setState({cover_image: event.target.value});
  }

  handleContentChange = ( event ) =>{
    this.setState({content: event.target.value});
  }

  handleAuthorChange = ( event ) =>{
    this.setState({author: event.target.value});
  }

  render (){
    const { result } = this.state;
    return (
        <div className="App">
         <h1>News API</h1>
         {this.state.link}
         <form onSubmit = {this.handleSubmit}>
           <p><input type = "text" placeholder = "link" name="link" value ={this.state.link} onChange={this.handleLinkChange}></input></p>
           <p><input type = "text" placeholder = "title" name="title" value ={this.state.title} onChange={this.handleTitleChange}></input></p>
           <p><input type = "text" placeholder = "date" name="date" value ={this.state.pub_date} onChange={this.handlePubDateChange}></input></p>
           <p><input type = "text" placeholder = "category" name="category" value ={this.state.category} onChange={this.handleCategoryChange}></input></p>
           <p><input type = "text" placeholder = "cover_image" name="cover_image" value ={this.state.cover_image} onChange={this.handleImageChange}></input></p>
           <p><input type = "text" placeholder = "content" name="content" value ={this.state.content} onChange={this.handleContentChange}></input></p>
           <p><input type = "text" placeholder = "author" name="author" value ={this.state.author} onChange={this.handleAuthorChange}></input></p>
           <p><button type="button" onClick={this.handleGet}>GET</button></p>
           <p><button type="button" onClick={this.handlePost}>POST</button></p>
         </form>
         {result.map(attribute => <div>{attribute.id}</div>)}
         {result.map(attribute => <div>{attribute.title}</div>)}
         {result.map(attribute => <div>{attribute.pub_date}</div>)}
         {result.map(attribute => <div>{attribute.category}</div>)}
         {result.map(attribute => <div>{attribute.cover_image}</div>)}
         {result.map(attribute => <div>{attribute.content}</div>)}
         {result.map(attribute => <div>{attribute.author}</div>)}
        </div>
      );
    }

    handleGet = ( event ) =>{
      const url = this.state.link;
      fetch(url).then(response => response.json())
      .then(data => this.setState({ result: data }))
    
      }
  
    handlePost = ( event ) =>{
      event.preventDefault();
      let details = {
            'title':this.state.title, 
            'pub_date':this.state.pub_date, 
            'category':this.state.category, 
            'cover_image':this.state.cover_image,
            'content':this.state.content,
            'author':this.state.author
    };
  
    let formBody = [];

    for (let property in details) {
      let encodedKey = encodeURIComponent(property);
      let encodedValue = encodeURIComponent(details[property]);
      formBody.push(encodedKey + "=" + encodedValue);
    }

    formBody = formBody.join("&");
  
    fetch(constants.BASE_URL + constants.POST_ARTICLE, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
      },
      body: formBody
    })
    
      }
}



export default newsAPI;
