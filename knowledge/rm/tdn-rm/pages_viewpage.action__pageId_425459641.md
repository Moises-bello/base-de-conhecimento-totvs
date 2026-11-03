---
content_hash: 5cf74ff6dd3d6f7406c77ae6e6a21f5e8ef71cdcc3ce964a16183c21040ad704
fetched_at: '2026-06-29T00:09:37.878036+00:00'
page_id: '425459641'
product: rm
source: tdn-rm
title: Dimensões Comuns
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459641
version: 3
---

**Dimensões Comuns**

---

As tabelas de dimensões Comuns possuem o nome com três caracteres. São as seguintes tabelas utilizadas na Stage Area:

* HG0 (CFOP)
* HG1 (Família Comercial) \*\*\*
* HG2 (Família Material) \*\*\*
* HG3 (Grupo de Estoque) \*\*\*
* HG4 (Portador*)* \*\*\*
* HG5 (Nível Hierárquico)
* HG6 (Tipo de Curso)
* HG7 (Tipo Motivo)
* HJ0 (Grupo Cliente)
* HJ1 (Unidade de Negócio) \*\*\*\*
* HJ2 (Transportadora)
* HJ3 (Produto Comercial)
* HJ4 (Empresa)
* HJ5 (Centro de Custo)
* HJ6 (Moeda)
* HJ7 (Cliente)
* HJ8 (Item)
* HJ9 (Natureza de Operação) \*\*\*
* HJA (Condição de Pagamento)
* HJB (Região - Região Geográfica, País, Estado e Cidade)
* HJC (Representante)
* HJD (Depósito)
* HJE (Conta Contábil)
* HJF (Forma - Modalidade - de Pagamento)
* HJG (Espécie de Documento a Pagar)
* HJH (Referencia) \*\*\*\*
* HJI (Tipo de Horas) \*\*\*\*
* HJJ (Período Extração)
* HJK (Parâmetro Extração)
* HJL (Curso)
* HJM (Colaborador)
* HJN (Instituição)
* HJ0 (Instrutor)
* HJP (Cargo)
* HJQ (Mão de obra)
* HJR (Evento)
* HJS (Motivo)
* HJT (Categoria Salarial)
* HJU (Turno)
* HJV (Sindicato)
* HJX (Planejador) \*\*\*\*
* HJY (Grupo Máquina) \*\*\*\*
* HJZ (Comprador)
* HK0 (Motivo Rejeição) \*\*\*\*
* HK1 (Situação de Crédito)
* HK2 (Período)
* HK3 (Fatos)
* HK4 (Áreas)
* HK5 (Planos de Contas)
* HK6 (Tipo de Movimento)
* HK7 (Origem) \*\*\*\*
* HK8 (Faixa Etária) \*\*\*\*
* HK9 (Grupo Instrução)
* HKA (Situação do Colaborador)
* HKC (Moeda Extração) \*\*\*\*
* HKD (Relação Trabalho)
* HKE (Estado Civil)
* HKF (Plano Centro Custo) \*\*\*\*
* HKG (Faixa Salarial)
* HKH (Tempo Casa)
* HKI (Tempo Cargo)
* HKJ (Fornecedor)
* HKK (Estabelecimento)
* HKN (Qualidade) \*\*\*\*
* HLN (Instancias)

(\*)Estas dimensões serão carregadas de acordo com as tabelas configuradas na visão de Parâmetros.

**(\*\*****)** Estas dimensões não serão contempladas nesta integração (Linha RM).  
    
 Os conceitos que serão utilizados para carga destas dimensões são:

* Dimensão - Cargo
* Dimensão - Categoria Salarial
* Dimensão - Centro Custo
* Dimensão - CFOP
* Dimensão - Cliente
* Dimensão - Colaborador
* Dimensão - Comprador
* Dimensão - Condição de Pagamento
* Dimensão - Conta Contábil
* Dimensão - Curso
* Dimensão - Depósito
* Dimensão - Empresa
* Dimensão - Espécie Documento – A Pagar
* Dimensão - Estabelecimento
* Dimensão - Estado Civil
* Dimensão - Evento
* Dimensão - Faixa Etária \*\*\*
* Dimensão - Faixa Salarial
* Dimensão - Família Comercial
* Dimensão - Família Material
* Dimensão - Fatos
* Dimensão - Forma (Modalidade) de Pagamento
* Dimensão - Fornecedor
* Dimensão - Grau de Instrução
* Dimensão - Grupo Cliente
* Dimensão - Grupo de Estoque
* Dimensão - Grupo Máquina \*\*\*
* Dimensão - Instâncias \*\*\*
* Dimensão - Instituição
* Dimensão - Instrutor
* Dimensão - Item
* Dimensão - Moeda Extração \*\*\*
* Dimensão - Moeda
* Dimensão - Motivo Rejeição \*\*\*
* Dimensão - Motivo
* Dimensão - Mão-de-obra
* Dimensão - Natureza de Operação
* Dimensão - Nível Hierárquico
* Dimensão - Origem \*\*\*
* Dimensão - Parâmetro Extração
* Dimensão - Período Extração
* Dimensão - Período
* Dimensão - Planejador \*\*\*
* Dimensão - Plano de Contas
* Dimensão - Portador
* Dimensão - Produto Comercial
* Dimensão - Região
* Dimensão - Relação Trabalho
* Dimensão - Representante
* Dimensão - Sindicato
* Dimensão - Situação Colaborador
* Dimensão - Situação Crédito \*\*\*
* Dimensão - Tempo Cargo
* Dimensão - Tempo Casa
* Dimensão - Tipo Curso
* Dimensão - Tipo Horas \*\*\*
* Dimensão - Tipo Motivo
* Dimensão - Tipo Movimento
* Dimensão - Transportadora
* Dimensão - Turno
* Dimensão - Unidade Negócio \*\*\*
* Dimensão - Áreas

(\*)Excepcionalmente estes conceitos não serão contemplados nesta integração (Linha RM).  
    
 Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
