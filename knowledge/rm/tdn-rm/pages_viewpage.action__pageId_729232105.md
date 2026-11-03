---
content_hash: 9d35bd6a20827eea3a939d27f6e03423c21785a85c0a5cdeefb014d7e8530fae
fetched_at: '2026-06-29T00:11:27.718823+00:00'
page_id: '729232105'
product: rm
source: tdn-rm
title: Candidatos e responsáveis menor de idade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729232105
version: 2
---

Uma inscrição permite que o candidato possa ser seu próprio responsável financeiro e ou acadêmico, ou seja cadastrado uma nova pessoa para cada papel ou aproveitado dados de outras pessoas, até mesmo pode ser utilizado a filiação do candidato para ser responsável financeiro ou acadêmico, caso o processo seletivo em questão esteja configurado para exibir estes dois papeis, sem nenhuma restrição de idade.

Por questões jurídicas da instituição e definições legais relacionadas a LGPD, a instituição pode optar por impedir que seja vinculado um responsável financeiro e ou acadêmico menor de idade.   
Com base nesta definição foi criado um parâmetro que impedirá que uma pessoa menor de idade seja vinculada como responsável financeiro e ou acadêmico, independente se for o próprio candidato ou uma de suas filiações.

Importante

Este parâmetro estará disponível para seleção após a execução do scritp CN.2022.12\_06 disponível nas versões 12.1.2205.210, 12.1.2209.154 e 12.1.2302 disponível em Fevereiro de 2023.

Quando o parâmetro: "Não permitir associar responsável financeiro e/ou acadêmico menor de 18 anos ao candidato" estiver marcado o sistema irá fazer a validação da idade de todos os papeis do processo seletivo.

Caso seja informado um candidato menor, quando na etapa de responsáveis, este não será exibido nem mesmo como uma opção para seleção como responsável financeiro e ou acadêmico.   
Caso a filiação seja também menor de idade, estas não serão exibidas para aproveitamento como responsável financeiro e ou acadêmico.

Somente serão exibidos nessa lista o candidato e ou filiações que forem maior de idade.

Caso seja cadastrado uma nova pessoa no papel de responsável financeiro e ou acadêmico o sistema também irá consistir e não permitirá prosseguir com a inscrição exibindo a seguinte mensagem.
