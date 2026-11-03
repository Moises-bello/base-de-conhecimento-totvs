---
article_id: 360018109012
category: RH - Rescisão
content_hash: 08d5e4a367ae4ecb5bfd8a8c3db5c71c88205e802b1a082746ef28ea2bfc645b
fetched_at: '2026-06-28T22:43:51.036466+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  É possível incluir verbas para funcionários demitidos?
type: support-article
updated_at: '2025-06-16T18:44:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018109012-RH-Linha-Protheus-GPE-%C3%89-poss%C3%ADvel-incluir-verbas-para-funcion%C3%A1rios-demitidos
---

**Dúvida**É possível incluir verbas para funcionários demitidos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O sistema permite a inclusão de verbas para funcionário demitidos através da rotina Lançamentos/ Por funcionário, mas no momento da inclusão é gerado uma mensagem informando que o funcionário esta com a situação de Demitido no cadastro. A mensagem de alerta não impede a ação de incluir uma verba.

Ao lançar a verba para o funcionário Demitido e calcular uma Rescisão Complementar, o sistema puxa automaticamente esse lançamento para o grid.

Caso a empresa queira impedir que em Lançamentos por funcionário ou Lançamento por verbas sejam incluídos valores para funcionários demitidos (Campo RA\_SITFOLH = "D"), deve incluir manualmente, através do Configurador (SIGACFG), o parâmetro **MV\_DEMISRC** com as seguintes configurações:

Filial :  
Nome da Var.: MV\_DEMISRC  
Tipo : C  
Descricao : Permitir a Alteracao ou Inclusao, em Valores Varia  
Cont.Descric: veis ou Valores Por Verba, para Funcionarios Demit  
Cont.Descric: idos. S=Sim, N=Nao.  
Conteudo : S ou N  
SIGAGPE : X  
  
**Observação**: Com o parâmetro como "N", os lançamentos são permitidos somente através da rotina de rescisão.
