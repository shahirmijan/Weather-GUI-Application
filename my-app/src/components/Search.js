import {Async} from 'react-select';
import React, { Component } from 'react';
import "../index.css";

class Search extends Component {
        render()
        {
            const
                getOptions = (input) => {
                    return fetch(`/uniName/${input}.json`)
                        .then((response) => {
                            return response.json();
                        }).then((json) => {
                            return {options: json};
                        });
                }

            const
                changeUni = (uni) => {
                    if (localStorage.uni !== uni) {
                        var coords = fetch(`/uniLocation/${uni}.json`).then((response) => {
                            return response.json()
                        });
                        localStorage.uni = uni;
                        localStorage.lat(coords[0]);
                        localStorage.lon(coords[1]);
                        window.location.reload();
                    }
                }
            return (
                <Async
                    className="searchBar"
                    name="uni-search"
                    value = "Enter University"
                    loadOptions={getOptions}
                    onChange={changeUni}
                />
            );
        }
};

export default Search;