---
content_hash: 1407a456c444e6ca0ebf4dc3189e95faad0c8e377a08227be1a45a3e9b0275f6
fetched_at: '2026-06-29T00:11:17.062245+00:00'
page_id: '676576795'
product: rm
source: tdn-rm
title: Matricula com Concurso de Bolsa
type: documentation
url: https://tdn.totvs.com/display/LRM/Matricula+com+Concurso+de+Bolsa
version: 5
---

Versão disponível

Esta funcionalidade está disponível a partir da versão 12.1.2205

# Descrição

Ao realizar a matricula de um candidato que alcançou uma bolsa através do concurso de bolsa o TOTVS Educacional vinculará automaticamente a bolsa alcançada no contrato do aluno.

É possível identificar se o candidato tem direito a bolas consultando o anexo "**Classificados concurso bolsa**", este anexo esta disponível através do cadastro do processo seletivo ou área de interesse ofertada.

Matrícula via central do candidato – Etapa “Plano de pagamento”

Durante a matricula via central do candidato na etapa "Planos de pagamento", os valores simulados serão exibidos considerando o abatimento da bolsa alcançada pelo candidato, e com isso será exibido na página a mensagem orientando ao usuário.

*Nota: No exemplo acima o candidato alcançou uma bolsa através do concurso de bolsa que esta parametrizado para aplicar a bolsa somente da parcela 1 a 2.*

O vinculo da bolsa com o contrato acontecerá exatamente no momento da inclusão do contrato para o aluno, essa inclusão poderá ocorrer nos seguintes cenários:

Ao incluir uma **bolsa** no contrato do aluno é necessário associar um determinado serviço, e para identificar quais serviços serão utilizados avaliamos as parcelas cadastradas para o contrato, portanto para que a **bolsa** seja inserida automaticamente é necessário que o contrato cadastrado seja gerado a partir de um plano de pagamento, pois com isso no momento da inclusão do contrato também serão cadastradas as parcelas e logo na sequência a **bolsa**.

Matricula via central do candidato

Para que o contrato seja incluído automaticamente na matricula via central do candidato, o cadastro da "Área de interesse ofertada" deve esta com a opção "**Cadastrar contrato**" marcada, e para que a bolsa seja incluída automaticamente um **plano de pagamento** deverá ser informado ou marcar a opção "**Permite alterar o plano de pagamento no Portal**"

Importante: mesmo que a opção "**Permite alterar o plano de pagamento no Portal**" esteja marcado deve ser observado se existem planos de pagamentos que serão exibidos na  matricula via central do candidato.

Importante

É necessário que o usuário "**RMProcessoSeletivo**" esteja cadastrado no RM, pois internamente é utilizado estes usuário para executar a inclusão da bolsa no contrato, e  o mesmo estará identificado como usuário de inclusão no cadastro da bolsa no contrato.

Se o usuário "**RMProcessoSeletivo**" não estiver cadastrado será apresentado a mensagem abaixo.

Matricula do processo seletivo via RM

Para que o contrato seja incluído automaticamente na matricula via RM, é necessário marcar a opção "**Cadastrar contrato**" e definir um "**Plano de pagamento**".

Processo de "Inclusão de contrato para alunos "Inclusão manual de contrato via TOTVS Educacional

Ao cadastrar manualmente o contrato para que a bolsa seja incluída automaticamente deve ser informado um **plano de pagamento.**

Após a inclusão do contrato respeitando as regras relatadas anteriormente a bolsa será vinculada automaticamente no contrato do aluno.

Os itens destacadas na imagem abaixo serão carregados das informações do cadastro do concurso de bolsa vinculado ao processo seletivo ou área de interesse ofertada e da classificação do candidato para o concurso de bolsa.

Será inserido no campo "**Observação**" do cadastro da bolsa as informações do processo seletivo e área de interesse ofertada.

Veja também:

[Concurso de bolsa](https://tdn.totvs.com/display/LRM/Concurso+de+Bolsa)

[Apuração do concurso de bolsa](https://tdn.totvs.com/pages/viewpage.action?pageId=663602469)
