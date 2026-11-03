---
article_id: 360042817574
category: Financeiro - Contas a Receber - LCDPR
content_hash: 8c1580fdc699debf48134edc66fc7bdd49ccc210f6a91fec3dfa12b60a50ba8f
fetched_at: '2026-06-28T22:38:15.834703+00:00'
product: protheus
section_id: 1500001539361
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Geração do extrator
  e processos do LCDPR
type: support-article
updated_at: '2023-02-14T17:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042817574-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Gera%C3%A7%C3%A3o-do-extrator-e-processos-do-LCDPR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:10:00 min**

**Dúvida**Como realizar a geração do arquivo para o LCDPR e configuração dos processos ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Financeiro – A partir da versão 12

**Solução**

Objetivo principal do **Wizard** é possibilitar ao operador a geração do arquivo do **Livro Caixa Digital do Produtor Rural** de acordo com a parametrização por ele definida.

**Obrigatoriedade**:  
Para saber se você está obrigado a entregar o **Livro Caixa Digital do Produtor Rural**, acesse: <http://receita.economia.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/lcdpr-livro-caixa-digital-do-produtor-rural>

**Para tanto, como pré-condições será necessário:**- Ter no mínimo o **Cadastro de um Imóvel** / **Filial** (vide Cadastro de Imóveis em Conteúdos Relacionados);

- Estar cadastrado como **Declarante** (vide Cadastro de Pessoas em Conteúdo Relacionado) do **LCDPR**em ao menos um dos imóveis;

- Ter ao menos uma **Conta de Banco** cadastrada como "Titularidade Própria" no **Cadastro de Bancos**(**tabela SA6**).

         Como resultado, o arquivo será gerado com base nas movimentações financeiras (**tabela SE5**),da(s) filial(ais) (que são os imóveis) selecionadas, e que possuam naturezas financeiras com o cadastro de '**Gera LCDPR  ?**' igual a '**Sim**'.

       Toda a movimentação que for realizada em um dos bancos indicados no **Extrator** **LCDPR** como sendo de titularidade do Declarante, será impressa no bloco **'Q',** de movimentação, com o código identificador da conta bancária.

       Se a movimentação possuir uma natureza financeira que '**Gera LCDPR ?**' = '**Sim**', mas a conta não for declarada, será apresentada como '**Numerário em Trânsito**' (**código '999'**).

       Já para os casos em que a transação for paga em dinheiro (motivo de baixa igual a '**Espécie**'), será apresentada como **pagamento em Espécie** (**código '000'**).

       Ainda no bloco de movimentações. os tipos de documentos identificados (no padrão) são:

- Nota Fiscal (tipo de documento = '**NF**');  
- Fatura (tipo de documento = '**FT**');  
- Recibo (tipo de documento = '**RC**');  
- Contrato (tipo de documento = '**C01**');  
- Folha de pagamento ((tipo de documento = '**FOL**');  
- Outros (demais tipos de documentos)

1. O **Wizard** será apresentado na tela para a definição de alguns parâmetros iniciais para geração da obrigação.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058421873/mceclip0.png)

2. Preencher com os parâmetros iniciais para geração do arquivo **LCDPR**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058421933/mceclip1.png)

3. Código do Proprietário (consulta direta do **Cadastro de Pessoas**, filtrando os declarantes):

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569374/mceclip2.png)

4. **Forma de apuração:** A forma de apuração do resultado da atividade rural adotada, indica que a pessoa física apurou o resultado com base no:

**Livro Caixa:** Apurou o resultado da atividade rural com base nos lançamentos registrados no Livro Caixa do Produtor Rural; ou

**Apurou o resultado** da atividade rural com base na faculdade disposta no art. 5º da Lei nº 8.023, de 1990 (20% da Receita Bruta).

**Situação Especial:**indicador de Situação Especial e Outros Eventos:

0 - Normal;

1 - Falecimento;

2 - Espólio;

3 - Saída definitiva do País.

**Data Situação Especial:**Data da Situação Especial: em caso de falecimento da pessoa física, a data de falecimento.

**Indicador do início do período:**Período esse que pode ser:

0 - Regular (Início no primeiro dia do ano);

1 - Abertura (Início de atividades no ano-calendário);

2 - Início da obrigatoriedade da escrituração no curso do ano calendário. (Exemplo: desenquadramento como isento do **IRPF**).

**Data inicial:** Data do início do período. Data inicial da informações contidas no arquivo. Este campo deve ser preenchido com a data inicial do período correspondente ao ano-calendário a que se referir o **LCDPR**.

**Data final:**Data final do período.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058422393/mceclip4.png)

5. Tela de seleção do **cadastro de imóveis**:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058422453/mceclip5.png)

6. Tela de seleção das **Contas** **Bancárias** do declarante:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569834/mceclip6.png)

7. Tela para definição do contador e diretório do arquivo:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569854/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057569874/mceclip8.png)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058422653/mceclip9.png)

**1) Dados necessário para geração do LCDPR**

Para validar os dados necessários para geração do LCDPR, validar pelo link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Dados necessários para configuração do LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042819814-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Dados-necess%C3%A1rios-para-configura%C3%A7%C3%A3o-do-LCDPR)

**2) Cadastro de Imóveis**

Para realizar o cadastro dos imóveis, validar pelo link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - Dados necessários para configuração do LCDPR- FINA029 – CADASTRO DE IMÓVEIS LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043296453-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Dados-necess%C3%A1rios-para-configura%C3%A7%C3%A3o-do-LCDPR-FINA029-CADASTRO-DE-IM%C3%93VEIS-LCDPR)

**3) Como utilizar o complemento de imóvel**

Para utilização do complemento de imóvel, validar o link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA029 - Como utilizar o complemento de imóvel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063879513-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA029-Como-utilizar-o-complemento-de-im%C3%B3vel)

**4) Cadastro de Pessoas**

Para realizar o cadastro das pessoas, validar pelo link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA031 - Cadastro de Pessoas LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042819514--Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA031-Cadastro-de-Pessoas-LCDPR)

**5) Como levar a inclusão do RA e PA para o livro caixa ao invés da compensação**

Para realizar a configuração, validar pelo link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA820 - Como levar a inclusão do PA ou RA no LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058883833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Como-levar-a-inclus%C3%A3o-do-PA-ou-RA-no-LCDPR)

**6) Qual CPF será levado para o extrator no momento da geração do extrator do LCDPR ?**

Para validar qual cpf será levado no momento da execução da rotina FINA820, validar pelo link abaixo:  
[Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFIN - FINA820 - Qual cpf será levado para o extrator do lcdpr no bloco Q100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063880833-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Qual-cpf-ser%C3%A1-levado-para-o-extrator-do-lcdpr-no-bloco-Q100)

**7) Como é apresentado o FUNRURAL no extrator do LCDPR**[Cross Segmento - TOTVS Backoffice (Linha Protheus) – SIGAFIN - FINA820 - Como é apresentado o FUNRURAL no LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413618167575-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Como-%C3%A9-apresentado-o-FUNRURAL-no-LCDPR)

**8) Pontos de entrada no LCDPR**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA820 - Pontos de entrada LCDPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043294773-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-Pontos-de-entrada-LCDPR)

**9) Atualização para o correto funcionamento do LCDPR no Protheus**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - LCDPR - Atualização para o correto funcionamento do lcdpr](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063881573-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-LCDPR-Atualiza%C3%A7%C3%A3o-para-o-correto-funcionamento-do-lcdpr)

**10) Extrator do LCDPR traz informações de títulos emitidos em ano diferente do range informado**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA820 - O Extrator do LCDPR traz informações de títulos emitidos em ano diferente do range informado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049715914-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA820-O-Extrator-do-LCDPR-traz-informa%C3%A7%C3%B5es-de-t%C3%ADtulos-emitidos-em-ano-diferente-do-range-informado)

**11) Perguntas e respostas frequentes do LCDPR - Receita Federal**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Perguntas e Respostas LCDPR - Receita Federal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048404273-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Perguntas-e-Respostas-LCDPR-Receita-Federal)

**12) How to LCDPR**

Cadastro 1 - <https://www.youtube.com/watch?v=lEYbcHOOvpw&t=3s>

Cadastro 2 - <https://www.youtube.com/watch?v=7ysaTNY_dhs&t=2s>

Extrator LCDPR - <https://www.youtube.com/watch?v=QysJ9GmN0Iw&t=3s>

**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=520110581>
