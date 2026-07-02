class Produto:
    def __init__(self, tipo_produto, marca, detalhes, valor_unitario, quantidade_disponivel, observacoes, status):
        self.tipo_produto = tipo_produto
        self.marca = marca
        self.detalhes = detalhes
        self.valor_unitario = valor_unitario
        self.quantidade_disponivel = quantidade_disponivel
        self.observacoes = observacoes
        self.status = status
        
    def cadastrar_produto(self):
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
            produto_encontrado.append(self.cadastrar_produto())
        return produto_encontrado
    
    def atualizar_produto(self, tipo_produto, marca, detalhes, valor_unitario, quantidade_disponivel, observacoes, status):
        self.tipo_produto = tipo_produto
        self.marca = marca
        self.detalhes = detalhes
        self.valor_unitario = valor_unitario 
        self.quantidade_disponivel = quantidade_disponivel
        self.observacoes = observacoes
        self.status = status
        
        return self.cadastrar_produto()
    
    def inativar_produto(self):
        self.status = "Inativo"
        return self.cadastrar_produto()
    
    def gerar_relatorio_produtos(self):
        relatorio = f"Tipo Produto: {self.tipo_produto}, Marca: {self.marca}, Detalhes: {self.detalhes}, Valor Unitario: {self.valor_unitario}, Quantidade Disponivel: {self.quantidade_disponivel}, Observações: {self.observacoes}, Status: {self.status}"
        return relatorio

class Mecanico:
    def __init__(self, nome, cpf, email, telefone, status):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.status = status
    
    def cadastrar_mecanico(self):
        mecanico = {
            "Nome": self.nome,
            "Cpf": self.cpf,
            "Email": self.email,
            "Telefone": self.telefone,
            "Status": self.status
        }
        return mecanico
    
    def buscar_mecanico(self, termo):
        encontrado = []
        if termo.lower() in self.nome.lower() or termo.lower() in self.cpf.lower():
            encontrado.append(self.cadastrar_mecanico())
        return encontrado
    
    def atualizar_mecanico(self, nome, cpf, email, telefone, status):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.status = status
        return self.cadastrar_mecanico()
    
    def inativar_mecanico(self):
        self.status = "Inativo"
        return self.cadastrar_mecanico()