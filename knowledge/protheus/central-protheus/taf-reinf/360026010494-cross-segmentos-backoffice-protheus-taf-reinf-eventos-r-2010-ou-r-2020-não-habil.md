---
article_id: 360026010494
category: TAF - REINF
content_hash: 594f555951c8c395bc1503d22e47a56fd4e1e921c7379807748ebd00ce4a2e37
fetched_at: '2026-06-28T22:41:33.568420+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  Eventos R-2010 ou R-2020
  não habilitam para a apuração.
type: support-article
updated_at: '2023-09-06T18:20:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026010494-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Eventos-R-2010-ou-R-2020-n%C3%A3o-habilitam-para-a-apura%C3%A7%C3%A3o
---

**Ocorrência**

Ao realizar todo o processo de integração das notas fiscais para o TAF, os eventos R-2010 e/ou R-2020 não estão habilitando para apuração.

![R2010R2020.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6165737551639)  
  
**Ambiente**

TAF – SIGATAF – A partir da versão 12.1.17  
  
**Causas**

* Falta de preenchimento na nota de campos obrigatórios;
* Notas não integraram para o TAF;
* Notas não foram levadas pelo Extrator Fiscal.

**Solução**

Para identificar onde está o problema, é preciso avaliar em etapas.

**Etapa 1**: **Avaliar se a nota está no TAF.**

1. O primeiro item é avaliar se as notas estão no TAF. Para isso, acessar o seguinte menu:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040569834)

2. Realizar um filtro pelo número da nota, da seguinte maneira:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040570194)

 OBS: Se as notas NÃO estiverem em Documentos de Entrada ou Documentos de Saída, ir para a etapa 2.

3. Se as notas estiverem em Documentos de Entrada ou Documentos de Saída, avaliar os seguintes campos:

[CROSS Segmentos - Backoffice Linha Protheus - TAF - REINF - Campos necessários para apuração R-2010 ou R-2020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044095634-CROSS-Segmentos-Backoffice-Linha-Protheus-TAF-REINF-Campos-necess%C3%A1rios-para-apura%C3%A7%C3%A3o-R-2010-ou-R-2020)

Caso algum dos campos acima não esteja de acordo, a nota não irá aparecer na apuração.

**Etapa 2: Avaliar se houve Erros no Gerenciador de Integração.**

1. Avaliar se as notas tiveram algum tipo de inconsistência no gerenciador de integração. Para isso, acessar o seguinte menu:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041398813)

2. Na seguinte tela, indicar a data que foi realizada a Integração, escolher o filtro por Fiscal:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041399053)

3. Neste tela, é apresentada os registros gerados como tickets, onde a legenda vermelha indica que um ou mais registros não foram integrados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041399393)

4. Clicando duas vezes na linha selecionada, abrirá uma tela indicando os layouts que foram integrados e os que não foram integrados:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041399613)

5. Clicando duas vezes, poderá ser visualizado o motivo da inconsistência, conforme exemplo abaixo:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041399673)

OBS: Se não houver nenhum registro do layout T013 na tela acima, verificar a etapa 3.

5. Inconsistências mais comuns no Gerenciador de Integração:

[MP - FIS - Layout T007 Código de origem C30\_ORIGEM inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020990791-MP-FIS-Layout-T007-C%C3%B3digo-de-origem-C30-ORIGEM-inexistente?source=search)

[MP - FIS - Layout T009 Natureza de operação C30\_NATOPE inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018331592-MP-FIS-Layout-T009-Natureza-de-opera%C3%A7%C3%A3o-C30-NATOPE-inexistente?source=search)

### [MP - FIS - Layout T010 Conta Superior C1O\_CTASUP inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018247691-MP-FIS-Layout-T010-Conta-Superior-C1O-CTASUP-inexistente?source=search)

[MP - FIS - Layout T013 Participante C20\_CODPAR inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022473971-MP-FIS-Layout-T013-Participante-C20-CODPAR-inexistente?source=search)

[MP - FIS - Layout T013 Conta Contábil C20\_CODCTA inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018252251-MP-FIS-Layout-T013-Conta-Cont%C3%A1bil-C20-CODCTA-inexistente?source=search)

[MP - FIS - Layout T013 Código do Item C30\_CODITE inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018478811-MP-FIS-Layout-T013-C%C3%B3digo-do-Item-C30-CODITE-inexistente?source=search)

[MP - FIS - Layout T013 Conta Contábil C30\_CTACTB inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017977992-MP-FIS-Layout-T013-Conta-Cont%C3%A1bil-C30-CTACTB-inexistente?source=search)

[MP - FIS - Layout T013 Centro de Custo C30\_CCUSTO inexistente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017512172-MP-FIS-Layout-T013-Centro-de-Custo-C30-CCUSTO-inexistente?source=search)

[MP - FIN - REINF- Layout T154 Não Integra com o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025784753-MP-FIN-REINF-Layout-T154-N%C3%A3o-Integra-com-o-TAF?source=search)

**Etapa 3: Avaliar se o layout T013 foi gerado.**

1. O Extrator Fiscal não encontrou a nota. Neste caso, avaliar a nota na origem:

[MP - TAF - REINF Como integrar o Layout T013 para o Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018105912-MP-TAF-REINF-Como-integrar-o-Layout-T013-para-o-Reinf?source=search)

Gerando o Extrator Fiscal em Arquivo TXT é possível avaliar se o T013 está sendo gerado.

2. Verificar se os parâmetros preenchidos no Extrator fiscal condizem com a situação da nota:

Período de extração: A data considerada na extração é a de entrada, não de emissão da nota.

Movimento: Validar se a pergunta está como ambos, caso queira levar notas de entrada ou saida.

Caso a pergunta esteja como Entrada e na extração conter notas de saída, ou vice versa, as notas não são levadas.

Espécie: Caso o campo espécie esteja preenchido, notas com espécie diferentes ou FT\_ESPECIE em branco não serão consideradas.

Cadastros: Caso um Produto/TES/Participante esteja deletado em sua tabela de origem (SB1, SF4, SA1/SA2) porém estiver referenciada na nota na SFT, o extrator pode não gerar o T013.
