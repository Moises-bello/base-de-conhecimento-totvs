---
article_id: 360051643973
category: RH - FGTS / SEFIP
content_hash: 99f45845e5303134af57df6ca1aec089857acbea55992711396de753c2971c88
fetched_at: '2026-06-28T22:43:41.296856+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro Sefip 320573 - Categoria do trabalhador não
  classificada como resolver ?
type: support-article
updated_at: '2023-04-28T21:15:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051643973-RH-Linha-Protheus-GPE-Erro-Sefip-320573-Categoria-do-trabalhador-n%C3%A3o-classificada-como-resolver
---

**Ocorrência**Ao importar o SEFIP apresenta o seguinte erro  320573-Categoria do trabalhador não classificada.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causas**- O PIS do trabalhador em questão esta duplicado em outro registro no cadastro do funcionário ou na tabela SRA.   
- Campo ocorrência incorreto ou em branco no cadastro de funcionário.  
  
**Solução****1**. Faça uma consulta genérica da tabela **SRA** e filtre o campo **RA\_PIS** com o código em questão e verifique quais registros estão com o mesmo PIS e veja se está mesmo duplicado. Caso esteja basta alterar e gerar a SEFIP novamente.  
**2.**Caso esteja duplicado, mas se trata de funcionário com múltiplo vinculo ou funcionário que tem um registro de aprendiz e foi contratado em outra matricula na mesma competência informe a ocorrência "05" no campo Ocorrência, da Aba "Funcionais" do cadastro de Funcionários.  
  
**Observação:**Ao alterar o campo de ocorrência dentro do cadastro de funcionário, se atende a data base do sistema, pois essa alteração irá gerar um registro na rotina Manutenção Hist. Funcionário (tabela SR9) e o sistema só tornará essa alteração válida a partir da data que foi realizada. Ex: Se você fizer a alteração no mês 06 e gerar a SEFIP do mês 05, o mesmo erro será gerado, pois a alteração foi posterior.

Caso a alteração tenha sido efetuada com a data incorreta, acessar a rotina através do caminho  Atualização / Funcionários / Manutenção Hist. Funcionário, e alterar o campo Dt. Alteração com a data da competência do SEFIP.

**OBS:** Caso não possua esta rotina no menu, efetue o procedimento conforme o link abaixo:

[RH - Linha Protheus - GPE - Como realizar manutenção no histórico de alterações do cadastro de funcionários (tabela SR9)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10724875306775-RH-Linha-Protheus-GPE-Como-realizar-manuten%C3%A7%C3%A3o-no-hist%C3%B3rico-de-altera%C3%A7%C3%B5es-do-cadastro-de-funcion%C3%A1rios-tabela-SR9)

**Saiba mais:  <https://tdn.totvs.com/display/public/PROT/FGTS>**
