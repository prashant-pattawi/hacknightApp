class HomesController < ApplicationController
  skip_before_action :verify_authenticity_token
  # GET /homes
  # GET /homes.json
  def index
    respond_to do |format|
      format.html { render(:file => 'homes/index.html.erb')}
    end
  end

  # GET /homes/1
  # GET /homes/1.json
  def show
  end

  # GET /homes/new
  def new
    @home = Home.new
  end

  # GET /homes/1/edit
  def edit
  end

  # POST /homes
  # POST /homes.json
  def create
    sleep(2)
    params.transform_values(&:downcase)
    command = "/home/joyc/anaconda3/bin/python #{Rails.root.to_s}/public/test.py '#{params.to_json}'"
    Rails.logger.info("running command: #{command}")
    out = `#{command}`
    Rails.logger.info("Got output: #{out}")
    return_val = YAML.load(out)
    render json: { data: return_val}
  end

  # PATCH/PUT /homes/1
  # PATCH/PUT /homes/1.json
  def update
    respond_to do |format|
      if @home.update(home_params)
        format.html { redirect_to @home, notice: 'Home was successfully updated.' }
        format.json { render :show, status: :ok, location: @home }
      else
        format.html { render :edit }
        format.json { render json: @home.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /homes/1
  # DELETE /homes/1.json
  def destroy
    @home.destroy
    respond_to do |format|
      format.html { redirect_to homes_url, notice: 'Home was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

end 
