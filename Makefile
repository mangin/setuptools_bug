clean:
	rm -rf library/.eggs library/dist library/mangin_library.egg-info
	rm -rf library_of_library/.eggs library_of_library/dist library_of_library/mangin_library_of_library.egg-info
	rm -rf project/.eggs projects/dist project/mangin_project.egg-info
release_library:
	cd library; \
	bump; \
	python3.7 setup.py sdist; \
	python3.7 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release_library_of_library:
	cd library_of_library; \
	bump; \
	python3.7 setup.py sdist; \
	python3.7 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
test:
	docker build .

