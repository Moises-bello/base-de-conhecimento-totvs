---
article_id: 10009154000407
category: Administração de Pessoal
content_hash: 7605a9dea818eda3e992881f8cc82dd8310b3647270e3503cac112016ba8a2e2
fetched_at: '2026-06-28T22:47:01.293764+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Alteração de Tomadores de serviços
type: support-article
updated_at: '2025-03-11T10:27:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10009154000407-RH-RM-FOP-Altera%C3%A7%C3%A3o-de-Tomadores-de-servi%C3%A7os
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:55 min****Dúvida**Como realizar a alteração de tomadores de serviços no módulo Folha de Pagamento, ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**A informação de tomadores de serviços no cadastro de funcionários serve para gerar o arquivo de SEFIP.RE e pode ter alterações periódicas. Existem duas opções para realização desta alteração dos tomadores.  
  
**1ª Opção:** A manutenção pode ser feita no cadastro do funcionário diretamente de forma rápida se for somente alguns. Para isso, acesse: **Administração de Pessoal | Funcionários | Selecione o funcionário desejado | Anexos | Histórico | Histórico de Rateio por Tomador**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10118133622295)

**2ª Opção****:** A manutenção pode ser feita através da rotina de alteração global de tomadores, na qual será útil caso haja necessidade de alterar um número maior de funcionários. Para isso, acesse: **Administração de Pessoal | Alteração Cadastrais | Alteração Tomadores**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10118250042519)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10118279074071)  
  
A consistência de dias informados por tomador de serviços para cada funcionário será feita gerando um log com inconsistências dos dias a distribuir x total de dias distribuídos, ou seja, será mostrado todos os funcionários que ultrapassaram os dias de trabalho em determinado mês.  
  
De acordo com a seleção utilizada, a rotina modifica os campos que são solicitados. Dentro desta seleção, sobrescreverá qualquer outra informação relativa à distribuição por tomadores no cadastro de funcionários pela informação especificada na rotina, ou seja, se existirem tomadores de serviço cadastrados nas respectivas pastas dos funcionários, estas informações serão apagadas e no lugar destas serão incluídas as informações cadastradas neste módulo. Com este módulo, será possível determinar a configuração de tomadores a ser adotada para uma quebra ou filtro especificado.  
  
**Importante**

* Tenha muita atenção para esta alteração porque será cadastrado tomador de serviços para todos os funcionários do filtro selecionado. Poderá ser alterado apenas dias de distribuição, caso não seja necessário a alteração do tomador de serviços. Neste caso somente será aceito um código que está sendo utilizado no Cadastro dos Funcionários em Tomadores de Serviços.
* Se não informar nenhum tomador, a alteração será realizada para todos os tomadores de serviços cadastrados no registro do funcionário. As informações de De/Para somente estarão disponíveis para alteração de apenas dias de distribuição. Confira o exemplo De/Para.
* A informação de **De/Para** será convertida para **Tipo** quando for solicitado **Determinar distribuição a todos os funcionários processado** para a seleção de qual **Tipo** de Tomador de serviço será marcado dentro da pasta de tomadores de serviço do funcionário.
* A alteração dos dias a serem distribuídos pelo tomador pode ser feita através de fórmula, como por exemplo, considerando os dias trabalhados do funcionário em determinado mês, deverá montar uma fórmula com o valor = ND. Confira o exemplo da Fórmula ND. **Dicas:**   
  - Alteração de 30 para 31 dias em empresas que têm funcionários horistas e mensalistas.  
  - Alterações de dias utilizando a fórmula ND para funcionários ativos, afastados no mês, retornos de afastamento, férias no mês, admitidos no mês e etc.
* Caso possua algum tomador que tenha data início anterior a competência atual, o processo irá criar uma data fim para esse tomador, para preservar o histórico e criará um novo com data atual.
* Caso o tomador selecionado no processo não exista no cadastro de Lotação Tributária, será disparado um gatilho de inclusão.

**Saiba Mais**[Exemplo De/Para](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718512)  
[Exemplo Fórmula ND](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718599)  
[Alteração de Tomadores](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719628)
