---
article_id: 360039829693
category: PMS - Projetos
content_hash: 251b8f11e3b79cbcb34f550f9ba4f7072717b2aaeb52a4c5ac1996f215f5af4b
fetched_at: '2026-06-28T22:37:15.059175+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: MP-PMS-Nível  do campo AFA_MOPC não pode ser alterado
type: support-article
updated_at: '2021-04-29T21:13:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039829693-MP-PMS-N%C3%ADvel-do-campo-AFA-MOPC-n%C3%A3o-pode-ser-alterado
---

**Dúvida** Pode se alterar o nível do campo do campo **AFA\_MOPC** ?

**Ambiente**

Microsiga Protheus - a partir da versão 11.  
  
**Solução**

Esse campo por padrão não pode ter o nível alterado, por que ele é um campo requerido na validação da getdados pela função **A203GD1LinOk** do fonte **PMSA203,** com  o nível padrão (1).

Além disso, ele trabalha em conjunto com o parâmetro **MV\_REPGOPC**  para direcionar a gravação dos opcionais no projeto, determinando se serão gravados no campo **AFA\_OPC** ou no campo memo **AFA\_MOPC**, isso é um requisito para o caso de tiver muitas ops a serem gravadas no projeto e aí o campo suportará maior quantidade de informação do que o campo **AFA\_OPC**.

Se mudar o nível padrão, o sistema gerará o erro  **array out of bounds ( 0 of 35 ) on A203GD1LINOK(PMSA203.PRW)**, sendo assim,por se tratar de um campo chamado dentro de  array para compor a rotina, deve permanecer ativo e com o nível 1.

Em caso de precisar tratar algo que o usuário venha digitar diretamente no campo, tente utilizar o ponto de entrada de validação de linha **A203LINOK1 (****<https://tdn.totvs.com/pages/releaseview.action?pageId=6795132>).**
