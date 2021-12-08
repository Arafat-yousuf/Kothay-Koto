import React from 'react';
import './Carousel.css';
import ReactCardCarousel from "react-card-carousel";
import SingleCard from '../SingleCard/SingleCard';

const Review = () => {
    return (
        <div className="carousel-container justify-content-center align-items-middle">
        <ReactCardCarousel autoplay={true} autoplay_speed={5000}>
          <SingleCard className="carousel-card">First Card</SingleCard>
          <SingleCard className="carousel-card">Second Card</SingleCard>
          <SingleCard className="carousel-card">Third Card</SingleCard>
          <SingleCard className="carousel-card">Fourth Card</SingleCard>
          <SingleCard className="carousel-card">Fifth Card</SingleCard>
        </ReactCardCarousel>
        </div>
    );
};

export default Review;