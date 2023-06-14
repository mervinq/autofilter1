from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("in & as Tesla ...")  # Replace [Your Name] with the appropriate name you want to use

app = web.Application()
app.router.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
