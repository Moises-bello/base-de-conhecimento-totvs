---
content_hash: ff4cc7cc9fafd448adb7d497cae538738897f13d6d0f3565de0e675393051c35
fetched_at: '2026-06-29T00:10:53.033669+00:00'
page_id: '574384400'
product: rm
source: tdn-rm
title: Importar XML Fila de Eventos eSocial
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+XML+Fila+de+Eventos+eSocial
version: 26
---

## **ÍNDICE**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01.****VERSÕES**

* 12.1.27.311
* 12.1.28.219
* 12.1.29.148
* 12.1.31.000

ATENÇÃO:

**Esse processo é exclusivo para clientes que utilizam o serviço Middleware.**

## **02.****VISÃO GERAL**

Através deste processo é possível realizar a importação do XML dos eventos do eSocial, sendo:

* + os baixados no site do governo, recuperando assim os eventos e respectivos recibos transmitidos para o eSocial, e/ou;
  + de ouros sistemas para carregamento de registros do legado para a fila de eventos em casos de migração de software de terceiros.

**OBSERVAÇÃO:**

* + Os eventos importados devem estar em formato XML.
  + Serão considerados somente os eventos periódicos e não-periódicos, exceto os eventos de SMT.

## **03. EXEMPLO DE UTILIZAÇÃO**

11Execução do scriptExecução do script

Para a liberação da importação do XML é necessário executar o script através do sistema RM.Atualizador.exe.

2ParametrizaçãoParametrização

Acesse o menu Serviços Globais | Segurança | Perfis, selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 09.05.14 - Importar XML

true3Importar XMLImportar XML

Acesse o menu RH | Folha de Pagamento | eSocial | Outros Processos | Importar XML, conforme tela abaixo:

Selecione a pasta onde estão os eventos que serão importados.

OBSERVAÇÃO:

O processo é dividido em duas pastas, sendo uma para os eventos que foram enviados ao RET e outra para os respectivos retornos, não poderão ter outros arquivos diferentes do descritos nesta pasta:

Após a seleção, clique em Executar:

O sistema irá apresentar um log da execução do processo, conforme demonstrado:

Os eventos importados ficarão disponíveis para visualização na fila de eventos:

IMPORTANTE:

Para a importação dos eventos referentes ao funcionário, é necessário que já possua seu cadastro no sistema, e para importação dos eventos periódicos é necessário que já possua o período de apuração criado.

4Importar XML eSocial downloads (BX)Importar XML eSocial downloads (BX)false

**A importação do XML Download (BX) está** **disponível** **a partir das versões:**

* 12.1.33.255
* 12.1.34.153
* 12.1.2205.100
* e Superiores.

Acesse o menu RH | Folha de Pagamento | eSocial | Outros Processos | Importar XML, conforme tela abaixo:

Selecione a pasta onde estão os eventos que serão importados:

OBSERVAÇÃO:

Será importado somente o XML retornado com as verbas enviadas e o recibo.

Após a seleção, clique em Executar:

O sistema irá apresentar um log da execução do processo, conforme demonstrado:

Os eventos importados ficarão disponíveis para visualização na fila de eventos:

IMPORTANTE:

Para a importação dos eventos referentes ao funcionário, é necessário que já possua seu cadastro no sistema, e para importação dos eventos periódicos é necessário que já possua o período de apuração criado.

5ErrosErros

* ERRO 1 - "Tipo de Evento inválido para importação!": Verifique se as pastas apontadas são dos xml's correspondentes, no processo apontamos pastas com o "**Localização do(s) XML(s) (Periodicos e Não-****Periodicos)**" e "**Localização do(s) XML(s)** **de Retorno"**, caso tenha xml's de retorno na pasta de "**Localização do(s) XML(s) (Periodicos e Não-****Periodicos)**" será apresentado o erro abaixo.

* ERRO 2 - Referência de objeto não definida para uma instância de um objeto : Verifique se o leiaute é o correto conforme seleção. Observação: caso seja o leiaute disponibilizado pelo governo é necessario marcar o parâmetro "Arquivos eSocial Download".

EXEMPLOS DE LEIAUTE.

* Importar XML: o xml aceito será no formato disponibilizado pelo sistema, para pegar exemplo do formato siga o passo a passo abaixo:

Exemplo **XML(s) (Periodicos e Não-****Periodicos)** acesse a fila de eventos e edite o xml na aba "Mensagem XML" e ir na opção "Salvar XML".

Exemplo **XML(s)** **de Retorno**acesse a fila de eventos e edite o xml na aba "Retorno da integração" e ir na opção "Salvar XML".

* eSocial downloads (BX): são xml's disponibilizados diretamente pelo [governo](https://www.gov.br/esocial/pt-br/empresas/orientacoes/esocial-bx-baixador-de-arquivos), a importação será somente o XML retornado com as verbas enviadas e o recibo, para permitir a retificação.

## **04. TABELAS UTILIZADAS**

* PESOCIALEVENTOS.

]]>
