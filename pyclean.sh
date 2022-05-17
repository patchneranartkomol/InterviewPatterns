#!/bin/sh

pyclean () {
	find . -regex '^.*\(__pycache__\|\.py[co]\)$' -delete
}

pyclean
