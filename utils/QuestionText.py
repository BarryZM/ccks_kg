# type2query = {
#     "人物": '社会中的以人为身份的个体，企业董事长，员工等都是人物；人物有姓名、年龄等属性；例如：钟南山、冯欣；',
#     "行业": '指一组提供同类相互密切替代商品或服务的公司；例如：交通运输、旅游业；',
#     "业务": '各行业中需要处理的事务，通常偏向指销售的事务；例如：住宅物业服务、维修；',
#     "产品": '做为商品提供给市场，被人们使用和消费，并能满足人们某种需求的任何东西；例如：奶粉、手机；',
#     "研报": '企业或者机构发布的公司或者行业的发展调查报告；有发布时间、评级、上次评级等属性；例如：证券研究报告/行业深度报告；',
#     "机构": '指政府、机关、团体等的内部组织；有全称、简称、英文名等属性；例如：美国国会、广汽集团；',
#     "风险": '指生产目的与劳动成果之间的不确定性；例如：行业政策风险、研发进度不达预期',
#     "文章": '用文字写成的，用于描述、记录或表达思想的文本，如各种手册、行业报告等等；文章有发布时间属性；例如：边缘计算专题报告、电商法',
#     "指标": '衡量目标的参数，预期中打算达到的指数、规格、标准，一般用数据表示；例如：市场占有率、利润率',
#     "品牌": '商业公司的产品或者业务的名称，也可以是公司名称；例如：小米集团、Note系列',
# }
type2query = {
    "指标": '衡量目标的参数，预期中打算达到的指数、规格、标准，一般用数据表示；例如：市场占有率、利润率',
    "品牌": '商业公司的产品或者业务的名称，也可以是公司名称；例如：小米集团、Note系列',
    "行业": '指一组提供同类相互密切替代商品或服务的公司；例如：交通运输、旅游业；',
    "业务": '各行业中需要处理的事务，通常偏向指销售的事务；例如：住宅物业服务、维修；',
    "产品": '做为商品提供给市场，被人们使用和消费，并能满足人们某种需求的任何东西；例如：奶粉、手机；'
}
query2type = {v: k for k, v in type2query.items()}