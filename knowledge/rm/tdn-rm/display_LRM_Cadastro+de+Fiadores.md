---
content_hash: a9984f84631c0b6695f4ee81e32a821ed46897b2fce6420d1db7e21ddfddea22
fetched_at: '2026-06-29T00:11:05.439507+00:00'
page_id: '631011716'
product: rm
source: tdn-rm
title: Cadastro de Fiadores
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+de+Fiadores
version: 25
---

**Acesse:** Financeiro / Contábil | Contratos | Fiadores ou Currículo e Oferta | Aluno e Professor | Alunos | Anexo - Fiadores

Foi disponibilizado no RM, apenas para o nível de ensino **superior**, o cadastro de fiador no TOTVS Educacional.

Agora é possível vincular a um aluno um cliente/fornecedor (**Categoria: Pessoa Física**) previsto como fiador no contrato de matrícula do aluno.

Um único fiador **ativo** é possível por matriz aplicada quando informada ou quando não informada este fiador estará disponível para qualquer  do aluno. Somente serão permitidos selecionar  que o aluno possui matricula no . O campo **status** indica qual é a situação deste fiador que foi realizada pela equipe financeira da Instituição de Ensino. Os **status** disponíveis são:

* **Em avaliação** - o cadastro do fiador foi realizado e esta sendo avaliado a documentação entregue;
* **Aprovado** - fiador aceito a estar vinculado ao aluno;
* **Reprovado** - fiador reprovado durante a avaliação da documentação e/ou avaliação interna da instituição. A reprovação de fiador exige que seja informado o motivo da reprovação, para isso uma nova aba é exibida.

Além disso, é possível vincular o fiador do aluno pelo anexo que se encontra dentro do cadastro do .

A partir do patch ****12.1.33****fiadores somente poderão ser aprovados se todos os documentos de seu anexo estiverem com o status de **validado**, caso contrário não será possível aprová-lo. Além disso, ao associar um fiador já associado a outro aluno e o mesmo estiver ativo, o sistema irá exibir uma mensagem de alerta dizendo que o fiador em questão está ativo e associado a outro aluno.

Somente é possível ter **dois fiadores iguais** cadastrados para **matrizes diferentes**. Caso queira que um fiador seja para todos os curso é necessário que crie o fiador sem preencher a matriz aplicada.

## **Troca de fiador**

A partir do patch **12.1.33**, foi disponibilizado ao aluno fazer a [troca de fiador no portal do aluno](https://tdn.totvs.com.br/display/LRM/Fiadores+do+Contrato+do+Aluno). Quando esse recurso de troca de fiador é utilizado, inicialmente o fiador a ser substituído entra no sistema **inativo** com status "**Em avaliação**".

Para a troca ser confirmada, status do fiador deverá ser modificado para "**Aprovado**", assim que o fiador foi armazenado nesse status, o sistema ativará esse fiador mudando esse fiador para aprovado na tabela SFIADOR e SCONTRATOFIADOR e mudará o fiador antigo para "**Substituído**" na tabela SCONTRATOFIADOR.

Caso deseje cancelar a troca, bastará mudar o fiador para o status "**Rejeitado**", assim que for armazenado, a troca será cancelada no sistema, o fiador antigo voltará para o status "**Aprovado**" na tabela SCONTRATOFIADOR e o fiador a ser substituído será removido em SCONTRATOFIADOR.

Informações Complementares

---
