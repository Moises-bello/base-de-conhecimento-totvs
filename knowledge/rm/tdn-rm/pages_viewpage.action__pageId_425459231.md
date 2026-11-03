---
content_hash: 89f2cb7f77473efe1643cb3f60009ae231d01f2b561b6b1d3e26aaff94c457c3
fetched_at: '2026-06-29T00:09:34.716196+00:00'
page_id: '425459231'
product: rm
source: tdn-rm
title: Mensagem Única
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459231
version: 5
---

**Mensagem Única**

---

As integrações que tem como base a arquitetura de Mensagem Única não são configuradas através da ferramenta Parâmetros.   
    
 Após rodar o configurador da integração, elas devem ser parametrizadas dentro da funcionalidade Mensagem Única.   
 Além da parametrização, toda a movimentação de mensagens, de-para, mapeamento de entidades, entre outros, são realizados dentro desta funcionalidade.   
    
 Ela é composta pelas opções:

* **Integrações:** na tela de Integrações estarão disponibilizadas todas as integrações com arquitetura de mensagem única que foi configurada na base. A integração irá aparecer após ter sido executado o configurador correspondente. São disponibilizadas as informações:

* Identificador: código identificador da integração
* Nome da Integração: nome completo da integração (exemplo: TOTVS Incorporação x BackOffice Protheus)
* Nome Reduzido: um nome reduzido da integração para identificar a mesma. (exemplo: TINPRO)
* Sistema Integrado: sistema ao qual o RM está sendo integrado (exemplo: Protheus)
* flag Ativo: se a integração deve ficar ativa ou não.  
      
   - URL Webservice: endereço do webservice do aplicativo informado no sistema integrado
* Autenticação (usuário e senha): usuário e senha de autenticação do webservice.  
   Algumas destas informações são preenchidas automaticamente pelo configurador. Outras devem ser informadas durante a configuração do ambiente da integração.Estão disponíveis os anexos Mapeamento de Atividades e Parâmetros da Integração. No primeiro estão disponíveis informações sobre as mensagens únicas utilizadas na integração. No segundo estão disponibilizados parâmetros da integração.  
      
   **Nota:** *informações específicas de cada integração estarão disponíveis no help da mesma.*

* **Transformação:** na tela de transformação estão armazenados os XSLT's, os quais são responsáveis por realizar a transformação do XML de Entrada para um XML no formato RM.
* **De-Para:** na tela de De-Para são apresentados os de-para criados ao longo das transações efetuadas na integração. Para cada registro sincronizado entre os aplicativos um de-para é criado. Através dele é possível rastrear o registro nos aplicativos, como por exemplo um cadastro de cliente sincronizado do software A para o software B. O de-para contém as informações:

* Tabela RM: nome da tabela do registro no lado RM.
* Chave Primária RM: campo que é chave primária da tabela no RM.
* Valor Chave Primária RM: valor da chave primária no RM. A chave primária não necessariamente é o código do registro no RM. A chave pode ser composta do código da coligada mais o código do registro, por exemplo. Isso vai depender de cada entidade.
* Sistema Integrado: nome do outro aplicativo (sem ser o RM).
* Valor Chave Integração: valor da chave do registro neste aplicativo. A chave primária não necessariamente é o código do registro no RM. A chave pode ser composta do código da coligada mais o código do registro, por exemplo. Isso vai depender de cada entidade.

* **Fila de Mensagens Únicas:** os sistemas integrados trocam mensagens ente si para sincronizar seus dados. As mensagens trocadas são gerenciadas na Fila de Mensagens Únicas. Nela estão disponibilizadas informações de cada mensagem trocada, como: Uuid da mensagem, identificador da transação, versão da mensagem, data de criação da mensagem, identificador da integração, qual o evento da mensagem, o tipo de entrega, se é entrada ou saída, e o XML original.

No anexo Informações de Execução de Mensagens é possível verificar o status da mensagem (se a transação ocorreu com sucesso ou se houve algum erro), bem como o XML da mensagem transformada e da mensagem de resposta.  
 Também está disponível o processo Execução Manual de Mensagens Únicas. Este processo prepara os registros selecionados para serem enviados/recebidos.

* **Agenda Execução da Fila:** tela para agendar processamento da fila, composta por Escalabilidade (se deseja dividir o processo em x partes), Hora da primeira execução (agora, executar em, ou sob demanda) e se deseja Repetir a Execução (não repetir, ou caso deseje repetir, informar os dados solicitados).

Voltar
