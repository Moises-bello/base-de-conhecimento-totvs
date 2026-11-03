---
content_hash: 72ab8177cd63cb26d936a543dc00b2da1d2374bf036bc6518e7c0730353f9305
fetched_at: '2026-06-29T00:09:29.787029+00:00'
page_id: '425458275'
product: rm
source: tdn-rm
title: Parâmetros Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458275
version: 25
---

Nesta guia define-se se será utilizada a integração com o Protheus. Caso positivo, devem ser informados os parâmetros de conexão com a base de dados:

### **Protheus**

* **Utiliza integração com o Protheus:** define se o sistema irá utilizar a integração financeira com o sistema Protheus.

### **Estoque, compras e faturamento**

* **Gera Movimento para Inscrição:** Habilita a integração do Processo Seletivo com o TOTVS Gestão de Estoque, Compra e Faturamento para que seja gerado movimento da inscrição do candidato.
* **Criar o cliente\fornecedor da inscrição a partir do:** Define se utilizará (se existe) ou criará o cliente\fornecedor do lançamento a partir do cadastro de candidato ou responsável.
* **Tipo de cliente\fornecedor:** define qual o Tipo do cliente\fornecedor será gerado
* **Serviço:** Define o serviço do TOTVS Gestão de Estoque, Compra e Faturamento que será utilizado para gerar o movimento da inscrição dos processos seletivos.
* **Histórico:** Define opcionalmente o preenchimento de um histórico. Poderão ser utilizadas as tags \[NUMEROINSCRICAO\], \[NOMECANDIDATO\] ou \[IDPS\] que serão substituídas pelo número da inscrição, nome do candidato ou identificador do processo seletivo de cada inscrição, respectivamente.
* **Regra Tributária**: cadastrar uma regra tributária, que permite **cadastrar uma Regra Tributária** e **vincular Regras Redutoras**, definindo como os tributos serão tratados nos contratos do sistema, conforme o **tipo de contrato** e as regras fiscais vigentes.

### **Gestão Financeira**

* **Ao efetuar o processo de cancelamento de inscrição do processo seletivo, cancelar automaticamente remessa do boleto:**Permite cancelar automaticamente a remessa bancária do boleto ao executar o processo de cancelamento de inscrição de um candidato em um processo seletivo. Quando marcado, o usuário será capaz de cancelar a inscrição de um candidato, sem antes ter que cancelar manualmente a remessa do boleto no TOTVS Gestão Financeira.
* **Valor de integração para guardar o desconto no lançamento do TOTVS Financeiro**

Valor de integração do TOTVS Financeiro que será responsável em guardar o valor de desconto no lançamento de inscrição do processo seletivo

* Este parâmetro está disponível somente a partir da versão 12.1.2406
* Para clientes que utilizam integração com o **Protheus** este parâmetro será obrigatório em função do recurso de baixa automática de lançamentos com 100% de desconto conforme a forma de inscrição, pois o Protheus não aceita a inclusão de lançamento com 100% de desconto, neste caso o valor do desconto será enviado nos valores de integração que será processado somente na baixa.
* O valor de integração selecionado deve-te a ação do tipo “**Desconta**”

### **Relacionamento com o cliente**

* **Atendente padrão para atendimentos criados à partir da inscrição no portal do processo seletivo:** Quando uma inscrição for feita pelo novo portal do processo seletivo e na  for definido um fluxo de trabalho para criação de um atendimento automaticamente no TOTVS Gestão de Relacionamento com o Cliente, é necessário preencher este parâmetro para que o atendimento seja criado corretamente.

  Importante

  Este parâmetro está disponível à partir das versões 12.1.27.328, 12.1.28.236 e 12.1.29.172.

### **Prova Fácil**

* **Dados de conexão:**
  + **Url de conexão com API:** Url de conexão com o ambiente do Prova Fácil para integrar processos seletivos.   
    A Url da API deve ser no formato: [https://[cliente].provafacilnaweb.com.br/[c](https://totvs-desenv.provafacilnaweb.com.br/totvs)liente]/, conforme o endereço de acesso ao ambiente do prova fácil.
  + **Usuário de autenticação da API:** Usuário criado no ambiente do Prova Fácil com permissão para conexão com a API.
  + **Senha**: Senha do usuário, a senha só é utilizada para carregar o Token, ao  salvar os parâmetros ela não será salva e ficará em branco.
  + **Carregar Token**: Realiza a conexão com a API, carrega o Token, o Token é utilizado em todas as requisições da integração com o Prova Fácil, assim este item é obrigatório para o correto funcionamento da integração.
* **Contexto**:

  + **Grupo empresarial**: informar qual a chave do parceiro do grupo empresarial (cadastro do Prova Fácil).
  + **Unidade de negócio:** informar qual a chave do parceiro da unidade empresarial (cadastro do Prova Fácil).
* **Tipo de avaliação**:
  + **Tipo de avaliação**: informar qual é a chave do parceiro do tipo de avaliação (cadastro do Prova Fácil).

Informações

Estes parâmetros estão disponíveis à partir da versão 12.1.32

Para mais informações sobre os parâmetros de integração com o Prova Fácil acesse:
