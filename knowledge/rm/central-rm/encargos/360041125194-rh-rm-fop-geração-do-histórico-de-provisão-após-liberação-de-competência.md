---
article_id: 360041125194
category: Encargos
content_hash: 4a9eb8f211de2c14600ae295a48d7c792809500524a954a29d69067e1cd70807
fetched_at: '2026-06-28T22:46:53.324743+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração do Histórico de Provisão após liberação de competência
type: support-article
updated_at: '2024-06-13T18:37:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041125194-RH-RM-FOP-Gera%C3%A7%C3%A3o-do-Hist%C3%B3rico-de-Provis%C3%A3o-ap%C3%B3s-libera%C3%A7%C3%A3o-de-compet%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24164230334871) Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Foi feita a liberação de competência sem que o Histórico de Provisão fosse gerado. Como proceder?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
**Solução**O transtorno pode ser causado quando o usuário não se atenta à necessidade de gerar o Histórico de Provisão antes da liberação de competência. Para evitar situações como esta, o sistema dispõe de uma opção que não permite a liberação de competência sem que o Histórico de Provisão seja gerado. A opção está presente em **Configurações | Parametrizador | Folha Normal | Contabilização | Provisão de férias/13º obrigatório**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13583524942615)  
  
Caso esta opção esteja marcada, ao tentar fazer a liberação de competência, o seguinte erro será apresentado no momento da validação:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13583627985815)  
  
Sugere-se, portanto, que esta opção seja utilizada para evitar maiores transtornos. Caso o incidente já tenha ocorrido, leia a seguir para verificar as propostas de solução.  
  
A princípio, não é possível gerar um Histórico de Provisão retroativo. Sendo assim, Há duas opções:  
  
**Opção 1 - Restauração de Backup**1. Nesta situação, é necessário que haja um backup de antes da liberação da competência. Restaurando o backup, será possível fazer a geração do histórico de provisão e exportar os dados para a sua base de produção através do Layout chamado: FOPLAY0024 09.003.008 Exportação de Históricos de Provisões. A estrutura do layout encontra-se disponibilizado no totvs compartilhamento, dentro do RM. Para importar o layout informado acima, siga as orientações da documentação a seguir:  
  
[RH - RM - FOP- Como importar relatórios através do totvs compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7781155867543-RH-RM-FOP-Como-importar-relat%C3%B3rios-atrav%C3%A9s-do-totvs-compartilhamento)  
  
2. Com o histórico de provisão gerado, exporte os dados através do layout cuja estrutura foi importada no sistema, seguindo o seguinte manual:  
  
[RM - BI - Como gerar layout no Gerador de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004522571-RM-BI-Como-gerar-layout-no-Gerador-de-Sa%C3%ADda?source=search)  
  
**3.** Desta forma, os dados já estarão consolidados num arquivo. Importe-o através do menu: Configurações | Importações | Importações de dados do RM Labore:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13583675106455)​  
  
4. Na janela que se abrirá, avance a primeira tela a selecione a aba "Históricos funcionário".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13583677634711)​  
  
5. Selecione a opção **Histórico de Provisões** conforme imagem acima, busque o arquivo de layout gerado e avance para concluir a importação dos dados.  
  
**Opção 2 - Elaboração do Layout**Este procedimento pode ser usado para evitar o uso de uma base de backup ou quando não se tem uma base de backup disponível. Neste caso, o procedimento terá caráter manual, mas possibilitará a entrada destes dados no sistema.  
  
Em resumo, o arquivo que é gerado através de layout padrão será gerado manualmente. A documentação a seguir contém a estrutura do layout a ser estruturado:  
  
[Layout Para Importação de Histórico de Provisões (Versão 12.1)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719349)  
  
Caberá ao usuário adicionar os valores correspondentes em cada campo, salvar o layout e importar através da opção **Importação de Dados do RM Labore**, conforme demonstrado na proposta de solução acima.  
  
**Importante**Temos nosso setor de Consultoria, que poderá via Banco de Dados, retornar a Competência do sistema para o Cliente, dessa forma, poderá gerar o Histórico de Provisão e depois retornar para a Competência atual, por ser um processo direto via Banco de Dados, é executado exclusivamente pela nossa Equipe de Consultoria, caso o Cliente tenha interesse, basta contatar a Consultoria ou solicitar via ticket esse procedimento, onde o Consultor fará o contato para informar as tarifas e ajuste.
