---
content_hash: 84fa5acd7b4c3b7736906b56244183c1b2eaeead80a3835fa32e28b815548de4
fetched_at: '2026-06-29T00:10:42.698130+00:00'
page_id: '547244984'
product: rm
source: tdn-rm
title: Cadastro Bancário e/ou Convênio (Totvs Incorporação x Backoffice Protheus -
  EAI2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547244984
version: 12
---

Os Processos descritos a seguir tem como objetivo orientar nos Cadastros de Bancos e Convênios para a Integração no Totvs Gestão de Imóveis x Backoffice Protheus - EAI2.

**Aviso**  
Antes de seguir os passos para cadastro de um banco e/ou convênio é recomendado que seja verificado as configurações de parametrização de integração.  
 entrar na aba "Cadastro de Adapter" que se encontra no link, os adapters utilizados para Banco (FINA130 - BANK) e Convênio (MATA070 - BANK)

# **Banco**

1. Abra o SmartClient do Protheus e logue no Módulo (SIGAFIN).
2. Vá no menu "Atualizações | Cadastros | Bancos", após abrir a visão de Bancos clique no botão Incluir na parte superior da tela.
3. No momento de preencher os dados do Banco no Protheus atente-se aos campos que são obrigatórios, caso venha a utilizar este banco para o cadastro de convênio.  

   Campos que são **obrigatórios** o preenchimento para que seja enviado o Convênio:

   * Codigo
   * Nro. Banco
   * Cod. Cedente (Este campo pode não estar visível no Protheus, porque ele não é utilizado no padrão, no Link de configuração tem a orientação de como habilitar o mesmo) [Como habilitar campo Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024437412-MP-SIGAFIN-Incluir-um-campo-da-mesma-tabela-no-browser-da-rotina)
4. Ao clicar em Salvar, os valores do Protheus serão enviados ao RM e ficará registrado na troca de mensagem pelo XML enviado, tanto no Protheus quanto no RM.
5. Obrigatório informar o nome da Filial no cadastro em SIGACFG - Pois o cedente busca o nome da Filial deste cadastro.

Importante

***Para visualizar a conta corrente com um descritivo mais intuitivo aos usuários do TCGI que possui uma conta corrente por Empreendimento.***  
Pode ser utilizado no cadastro do Protheus a separação da especificação da conta com ; no descritivo do nome do Banco Protheus, Isso fará com que seja acrescentado na descrição da Conta Caixa do RM que é utilizada em todos os processos de Recebíveis.  
  
**Exemplo:**  
Protheus campo "Nome Banco" = BANCO SAFRA;**BELO HORIZONTE**  
  
     Como ficará no RM:  
 Conta Caixa campo "Descrição" = **BELO HORIZONTE** - Banco 237 - Agência R03 - Conta 85621  
 Banco campo "Nome" = BANCO SAFRA

# **Convênio**

## - Contrato Bancário

1. Abra o SmartClient do Protheus e logue no Módulo (SIGAFIN).
2. Vá no menu "Atualizações | Cadastros | Contrato Bancário", após abrir a visão de Contrato Bancário clique no botão Incluir na parte superior da tela.
3. No momento de preencher os dados do Contrato Bancário no Protheus atente-se ao campo 'Numero'.

   Importante

   O valor informado neste campo deverá ser utilizado no próximo passo que irá enviar o convênio ao RM - "Parâmetros de Bancos".

- Parâmetros de Bancos

1. Vá no menu "Atualizações | Cadastros | Parâmetros de Bancos", após abrir a visão do Parâmetros de Bancos clique no botão Incluir na parte superior da tela.
2. Na aba "Cadastrais", Informar o Banco já cadastrado na base que será enviado o convênio.
3. Na aba "Outros", Informar o campo 'Contrato' com o mesmo valor do campo 'Numero' do Contrato Bancário cadastrado.
