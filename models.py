class Produto:
    def __init__(self, tipo_produto, marca, detalhes, valor_unitario, quantidade_disponivel, observacoes, status):
        self.tipo_produto = tipo_produto
        self.marca = marca
        self.detalhes = detalhes
        self.valor_unitario = valor_unitario
        self.quantidade_disponivel = quantidade_disponivel
        self.observacoes = observacoes
        self.status = status
    @classmethod
    def criar(cls, dados):
        return cls(
            dados["tipo_produto"],
            dados["marca"],
            dados["detalhes"],
            dados["valor_unitario"],
            dados["quantidade_disponivel"],
            dados["observacoes"],
            dados["status"]
        )    
    def to_dict(self):
        produto = {
            "Tipo produto": self.tipo_produto,
            "Marca": self.marca,
            "Detalhes": self.detalhes,
            "Valor unitario": self.valor_unitario,
            "Quantidade disponivel": self.quantidade_disponivel,
            "Observacoes": self.observacoes,
            "Status": self.status
        }
        return produto
    
    def buscar_produto(self, termo):
        produto_encontrado = []
        
        if termo.lower() in self.tipo_produto.lower() or termo.lower() in self.marca.lower():
            produto_encontrado.append(self.criar())
        return produto_encontrado
    
    def atualizar(self, tipo_produto, marca, detalhes, valor_unitario, quantidade_disponivel, observacoes, status):
        self.tipo_produto = tipo_produto
        self.marca = marca
        self.detalhes = detalhes
        self.valor_unitario = valor_unitario 
        self.quantidade_disponivel = quantidade_disponivel
        self.observacoes = observacoes
        self.status = status
        
        return self.criar()
    
    def inativar(self):
        self.status = "Inativo"
        return self.criar()
    
    def gerar(self):
        relatorio = f"""
        Tipo Produto: {self.tipo_produto}
        Marca: {self.marca}
        Detalhes: {self.detalhes}
        Valor Unitario: {self.valor_unitario}
        Quantidade Disponivel: {self.quantidade_disponivel}
        Observações: {self.observacoes}
        Status: {self.status}"""
        return relatorio

class Mecanico:
    def __init__(self, nome, cpf, email, telefone, status):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.status = status
    
    def criar(self):
        mecanico = {
            "Nome": self.nome,
            "Cpf": self.cpf,
            "Email": self.email,
            "Telefone": self.telefone,
            "Status": self.status
        }
        return mecanico
    
    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.nome.lower() or termo.lower() in self.cpf.lower():
            encontrado.append(self.criar())
        return encontrado
    
    def atualizar(self, nome, cpf, email, telefone, status):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.status = status
        return self.criar()
    
    def inativar(self):
        self.status = "Inativo"
        return self.criar()

class Estado:
    def __init__(self, nome, uf):
        self.nome = nome
        self.uf = uf
    
    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.nome.lower() or termo.lower() in self.uf.lower():
            estado = {
                "nome": self.nome,
                "UF": self.uf
            }
            encontrado.append(estado)
        return encontrado
        
class Cidade:
    def __init__(self, nome, cep, ibge: int, estado: Estado):
        self.nome = nome
        self.cep = cep
        self.ibge = ibge
        self.estado = estado
    
    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.nome.lower() or termo.lower() in self.cep.lower() or termo in str(self.ibge):
            cidade ={
                "Nome": self.nome,
                "CEP": self.cep,
                "IBGE": self.ibge
            }
            encontrado.append(cidade)
        return encontrado

class Cliente:
    def __init__(self, nome, cpf_cnpj, data_nascimento, email, telefone, logradouro, bairro, numero, cidade: Cidade, status):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.status = status
    
    def criar(self):
        cliente = {
            "Nome": self.nome,
            "CPF/CNPJ": self.cpf_cnpj,
            "Data Nascimetno": self.data_nascimento,
            "Email": self.email,
            "Telefone": self.telefone,
            "CEP": self.cidade.cep,
            "Logradouro": self.logradouro,
            "Bairro": self.bairro,
            "Numero": self.numero,
            "Cidade": self.cidade.nome,
            "Estado": self.cidade.estado.nome,
            "Status": self.status
        }
        return cliente

    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.cpf_cnpj.lower() or termo.lower() in self.email.lower():
            encontrado.append(self.cadastrar())
        return encontrado

    def atualizar(self, nome, cpf_cnpj, data_nascimento, email, telefone, logradouro, bairro, numero, cidade, status):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.cidade = cidade
        self.status = status
        return self.cadastrar()
    
    def inativar(self):
        self.status = "Inativo"
        return self.cadastrar()

class Agendamento:
    def __init__(self, data_solicitacao, data_agendada, tipo_servico, observacoes, status):
        self.data_solitacao = data_solicitacao
        self.data_agendada = data_agendada
        self.tipo_servico = tipo_servico
        self.observacoes = observacoes
        self.status = status
        
    def cadastrar(self):
        agendamento = {
            "Data Solicitação": self.data_solitacao,
            "Data Agendada": self.data_agendada,
            "Tipo Servico": self.tipo_servico,
            "Observações": self.observacoes,
            "Status": self.status
        }
        return agendamento

    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.data_solitacao or termo.lower() in self.tipo_servico:
            encontrado.append(self.cadastrar())
        return encontrado

    def atualizar(self, data_solicitacao, data_agendada, tipo_servico, observacoes, status):
        self.data_solitacao = data_solicitacao
        self.data_agendada = data_agendada
        self.tipo_servico = tipo_servico
        self.observacoes = observacoes
        self.status = status
        return self.cadastrar()

    def inativar(self):
        self.status = "Cancelado"
        return self.cadastrar()
    
    def gerar(self):
        relatorio = f"""
    Data Solicitação: {self.data_solitacao},
    Data Agendada: {self.data_agendada},
    Tipo Servico: {self.tipo_servico},
    Observações: {self.observacoes},
    Status: {self.status}
    """
        return relatorio
    
class Fornecedor:
    def __init__(self, cpf_cnpj, nome_razao_social, telefone, email, logradouro, cidade: Cidade, bairro, numero, status):
        self.cpf_cnpj = cpf_cnpj
        self.nome_razao_social = nome_razao_social
        self.telefone = telefone
        self.email = email
        self.cidade = cidade
        self.logradouro = logradouro
        self.bairro = bairro
        self.numero = numero
        self.status = status
    
    def criar(self):
        fornecedor = {
            "Nome": self.nome_razao_social,
            "CPF/CNPJ": self.cpf_cnpj,
            "Telefone": self.telefone,
            "Email": self.email,
            "Logradoruo": self.logradouro,
            "CEP": self.cidade.cep,
            "Cidade": self.cidade.nome,
            "Estado": self.cidade.estado.nome, 
            "Bairro": self.bairro,
            "Numero": self.numero,
            "Status": self.status
        }
        return fornecedor
    
    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.cpf_cnpj.lower() or termo.lower() in self.nome_razao_social.lower():
            encontrado.append(self.criar())
        return encontrado
    
    def atualizar(self, cpf_cnpj, nome_razao_social, telefone, email, logradouro, cidade, bairro, numero, status):
        self.cpf_cnpj = cpf_cnpj
        self.nome_razao_social = nome_razao_social
        self.telefone = telefone
        self.email = email
        self.logradouro = logradouro
        self.cidade = cidade
        self.bairro = bairro
        self.numero = numero
        self.status = status
        return self.criar()
    
    def inativar(self):
        self.status = "Inativo"
        return self.criar()
    
    
class Veiculo:
    def __init__(self, modelo, marca, placa, codigo_renavam, ano_fabricacao, ano_modelo, tipo_combustivel, chassi, cor, quilometragem, tipo_cambio, status):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.renavam = codigo_renavam
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.tipo_combustivel = tipo_combustivel
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
        self.tipo_cambio = tipo_cambio
        self.status = status
        
    def criar(self):
        veiculo = {
            "Modelo": self.modelo,
            "Marca": self.marca,
            "Placa": self.placa,
            "Renavam": self.renavam,
            "Ano Fabricação": self.ano_fabricacao,
            "Ano Modelo": self.ano_modelo,
            "Tipo Combustivel": self.tipo_combustivel,
            "Chassi": self.chassi,
            "Cor": self.cor,
            "Quilometragem": self.quilometragem,
            "Tipo Cambio": self.tipo_cambio,
            "Status": self.status
        }
        return veiculo
    
    def buscar(self, termo):
        encontrado = []
        if termo.lower() in self.chassi.lower() or termo.lower() in self.renavam.lower():
            encontrado.append(self.cadastrar_veiculo())
        return encontrado
    
    def atualizar(self, modelo, marca, placa, codigo_renavam, ano_fabricacao, ano_modelo, tipo_combustivel, chassi, cor, quilometragem, tipo_cambio, status):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.renavam = codigo_renavam
        self.ano_fabricacao = ano_fabricacao
        self.ano_modelo = ano_modelo
        self.tipo_combustivel = tipo_combustivel
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
        self.tipo_cambio = tipo_cambio
        self.status = status
        return self.cadastrar_veiculo()
    
    def inativar(self):
        self.status = "Inativar"
        return self.cadastrar_veiculo()