---
content_hash: 29fc389603e612ba7c28f4da76ba071b09c360efe043534447f8b26c521cc535
fetched_at: '2026-06-29T00:11:38.361343+00:00'
page_id: '784771955'
product: rm
source: tdn-rm
title: 01.04 Parâmetros de alteração de dados dos responsáveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=784771955
version: 1
---

Pai / Mãe 

Em concordância com a legislação realizamos um ajuste na apresentação das informações dos dados dos responsáveis para que não seja mais apresentado o descritivo “**Mãe**” ou “**Pai**”, agora será apresentado o descritivo “**Filiação 1**” e “**Filiação 2**”, sendo necessário indicar qual o tipo de filiação que será cadastrado.

Legislação:

***"A Lei de Registros Públicos (Lei nº 6.015/73) foi alterada em 2009, pela Lei nº 11.924, para tornar possível ter dois pais e duas mães no assento do nascimento da pessoa natural”***

Alterações disponíveis a partir das versões: 12.1.31.235, 12.1.32.170, 12.1.33.104

Tipo de filiação

Com a mudança do descritivo das informações para “**Filiação 1**” e “**Filiação 2**” foi criada uma nova parametrização "**Tipo de filiação obrigatório"** que permite definir o tipo de filiação que será obrigatório, sendo de total responsabilidade do cliente a parametrização.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Não se aplica"**, o sistema não irá fazer validação para algum tipo de filiação específico.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Pai"**, o sistema somente permitirá prosseguir caso seja informado **ao menos uma filiação** com o tipo **"Pai"**.

Caso o **Tipo de filiação obrigatório**seja marcado como **"Mãe"**, o sistema somente permitirá prosseguir caso seja informado **ao menos uma filiação** com o tipo **"Mãe"**.

Caso o **Tipo de filiação obrigatório**seja marcado como "**Ambos"**, o sistema somente permitirá prosseguir caso seja informado **uma filiação do tipo "Mãe" e uma do tipo "Pai".**

Opção disponível a partir da versão 12.1.32.213, 12.1.33.137, sendo necessário executar o **RM Atualizador**.

Responsável legal

A partir da versão 12.1.2302, prevista para Fevereiro de 2023, quando o processo seletivo for do ensino superior, será exibido nas opções de matrícula no cadastro de área ofertadas o parâmetro "Utilizar preenchimento obrigatório do Responsável Legal (Responsável Acadêmico)".

Ao ser marcado, indicará na matrícula através da central que caso o candidato que está sendo matriculado seja menor de idade, será obrigatório o preenchido do responsável legal, neste caso, atribuído ao papel do responsável acadêmico, mesmo que o este papel esteja desmarcado para preenchimento.

Dica

Para mais informações sobre a matrícula acesse:
