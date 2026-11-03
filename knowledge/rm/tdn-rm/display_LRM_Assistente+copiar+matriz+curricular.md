---
content_hash: 5e226e2425c7ab7650dc3e02c05f77833e261dc31425f7682717be579b6ba987
fetched_at: '2026-06-29T00:09:33.383475+00:00'
page_id: '425459006'
product: rm
source: tdn-rm
title: Assistente copiar matriz curricular
type: documentation
url: https://tdn.totvs.com/display/LRM/Assistente+copiar+matriz+curricular
version: 10
---

Este assistente facilita a montagem de novas matrizes curriculares, aproveitando os dados já informado em outras matrizes.

Através dele, é possível:

•  Criar uma nova matriz, com todas as configurações/valores cadastrados na matriz de origem.

•  Optar por incluir ou excluir disciplinas que farão parte da matriz curricular além de definir ou alterar em qual período as mesmas estarão associadas.

•  Alterar o Status da nova matriz curricular para Ativa, Inativa e Atual.

**Observação**:

1) Ao alterar a nova matriz curricular para Inativa, o sistema não permite que um aluno seja matriculado nesta matriz curricular.

2) Ao selecionar o status atual, o sistema obriga a mudar o status da matriz curricular que já possui o status definido como atual. Visto que somente uma matriz curricular do curso pode ser a atual.  
  
**Exemplo:** Selecionou para a nova matriz o status atual e o curso tinha outra que era atual, a outra passará a ter o status também definido no processo.  
• Copiar os dados das matrizes aplicadas, e também campos complementares.

Ao realizar a copia do Campus/Polo, o sistema verifica se o parâmetro Ativo que consta no cadastro do Campus/Polo da [matriz aplicada](https://tdn.totvs.com/display/public/LRM/Matriz+Aplicada), está marcado ou desmarcado na matriz de origem e gera a copia respeitando as informações da origem.

Além disso, existe o parâmetro oferta ativa na [matriz aplicada](https://tdn.totvs.com/pages/editpage.action?pageId=425458548) que permite habilitar ou desativar a matriz aplicada para a vinculação da oferta. 

Ao realizar o processo de copia da [matriz curricular](https://tdn.totvs.com/display/LRM/Matriz+Curricular), o sistema verifica na matriz curricular se possui matriz aplicada e replica a informação relativa a este campo oferta ativa, de acordo com a parametrização informada na matriz de aplicada de origem.

A partir das versões 12.1.2502.232, 12.1.2506.181, 12.1.2510.115 e 12.1.2602 este processo passa a copiar os campos de **Composição da Carga Horária** e da **Distribuição por Modalidade** do cadastro da  e os campos Presencial, À distância, Síncrona, Síncrona mediada e  Assíncrona da .

Veja Também

---

[Boletim Técnico: Copiar Matriz Curricular](http://tdn.totvs.com/download/attachments/185760819/EDU_BT_Copiar_Matriz_Curricular_PCREQ-3296%28C367128%29.pdf?version=1&modificationDate=1430161994000&api=v2)
