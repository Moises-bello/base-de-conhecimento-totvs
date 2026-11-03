---
content_hash: 8d6ec371995dc684588f87a8d4aa9ebcdf6d9e6c89b61895d5bc4480fe8f7c8a
fetched_at: '2026-06-29T00:09:35.339102+00:00'
page_id: '425459316'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Cadastro de Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/Linha+RM+x+Protheus+SigaMNT+-+Cadastro+de+Projeto
version: 2
---

**Linha** **RM x Protheus SigaMNT - Cadastro de Projeto**

---

As inclusões, alterações e exclusões de Projeto são feitos através do Linha RM, que identifica o evento em sua entidade e envia uma mensagem ao Protheus SigaMNT. Através da sincronia de dados o Protheus pode utlizar os projetos enviados , em seus processos de Manutenção de Ativos. Os dados sincronizados pela mensagem única são:

**Aba Identificação**

* Cód.Filial
* Cód.Projeto
* Descrição
* Código do Centro de Custo

**Anexos / Histórico do Projeto**

* Posição
* Data Mudança

**Menu construção e Projeto / Projeto / Cronograma / Períodos**

* Data de Início
* Data de Fim

**Observações:**

1. Os campos abaixo serão enviados ao Protheus SigaMNT somente quando o projeto  for alterado e salvo , porque  eles estão localizados em um menu diferente do menu de cadastro de projeto.
   * Data de Inicio
   * Data de Fim
2. Para correta parametrização  do  Projeto  é necessário que o aplicativo U\_UPDPMS seja executado.
3. Ao enviar um Projeto ao Protheus SigaMNT é criada uma referência  a um calendário de cronograma que deve ser criado  para cada uma das empresas.
4. O código da filial do projeto será sempre obrigatório caso a integração esteja instalada. Caso ele não seja informado será exibida uma mensagem ao usuário e a mensagem não será enviada ao Protheus.
5. O campo "Código do Projeto" no Protheus está limitado a 10 caracteres. Caso o RM possua Código do Projeto com mais de 10 caracteres deve-se analisar o Protheus deve ser configurado como autoincremento.
6. Quando o código do projeto e/ou código da filial do projeto é alterado, deve-se enviar uma mensagem de alteração de projeto. O Protheus ficará responsável em atualizar o seu De-Para e enviará ao RM uma mensagem contendo os novos InternalIDs criados.

Para mais informações sobre  U\_UPDPMS**,** Clique aqui  
 Para mais informações sobre a criação do Calendário ,Clique aqui  
 Para mais detalhes sobre o cadastro , acese o Boletim Técnico.

---

**Recursos Adicionais**

TDN - Boletim Técnico : [Projeto](http://tdn.totvs.com/download/attachments/76251248/CONNECTOR_BT_CADASTRAR+PROJETO_BR_CON000158.pdf?version=1&modificationDate=1380044701000)
