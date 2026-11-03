---
article_id: 19677367875607
category: Financeiro - Reinf
content_hash: e27ae6b37c1bc866b286cdade108382c7b3deb6e352f40fb07eb7767e9c793bb
fetched_at: '2026-06-28T22:37:51.762016+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O que fazer quando
  executamos o Extrator Fiscal e o registro do título não aparece no painel do TAF
type: support-article
updated_at: '2025-08-25T14:28:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19677367875607-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-que-fazer-quando-executamos-o-Extrator-Fiscal-e-o-registro-do-t%C3%ADtulo-n%C3%A3o-aparece-no-painel-do-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24350032882071)**Tempo aproximado para leitura: **01:00 min**

**Dúvida**

O que fazer quando executamos o Extrator Fiscal e o registro do título não aparece no painel do TAF?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

**1º Validar a tabela FKW e FKY**

Quando o parâmetro **MV\_BX10925= 2** (impostos gerados na emissão do título), será gerada a tabela FKW na inclusão do título com natureza de rendimento. Neste cenário, a **tabela FKW** será validada pelo extrator para o envio dos registros ao **painel TAF**.

Quando o parâmetro **MV\_BX10925= 1** (impostos gerados na baixa do título), será gerada a **FKW** ao incluir o título e a **FKY** ao realizar a baixa. Neste cenário, a tabela **FKY** será validada pelo extrator para o envio dos registros ao **painel TAF.**

**Importante**

Quando um título é incluído no módulo de compras ou no financeiro, com a natureza de rendimento vinculada, será gerada a tabela **FKW**, que reflete as informações destinadas ao painel do **TAF**.

Para localizar o título na tabela **FKW**, deve-se primeiramente consultar a tabela **FK7** e filtrar pelo número da nota e fornecedor. Com o **IDDOC** obtido nessa tabela, você conseguirá realizar o filtro correspondente na **FKW**.

![Gravar_2024_06_26_10_20_31_977.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24444330058647)

**IMPORTANTE:**

```
Caso as tabelas FKW ou FKY não sejam criadas, os dados não serão encaminhados ao TAF. Nesse cenário,  
somente excluindo o registro e registrá-la novamente ou adicionar as informações manualmente por meio   
do painel do TAF.
```

**2º Validar se houve baixa do título principal**

O fato gerador do Reinf é a baixa do título, validar se houve baixa total ou parcial. 

 

**3º  Validar os campos FKF\_REINF e FK2\_REINF**

Caso o conteúdo esteja marcado como 1, significa que foi processado pelo **extrator.**

Caso o conteúdo esteja igual a 2, esse registro ficará disponível para extração do tipo **banco a banco**.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/24458380841239)](https://tdn.totvs.com/pages/releaseview.action?pageId=819499423)

Ao executar o extrator fiscal, na tela do gerenciador de integração, será exibida a transmissão. Caso ocorra alguma inconsistência no processo, ficará com a legenda em vermelho. Clique sobre o registro processado, conforme exemplo abaixo, sendo possível identificar os registros com erro, neste exemplo, o **T013 e T154**.

![Gravar_2024_06_26_11_15_44_791.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24446334073239)

Clicando sobre o registro, exemplo **T154** será exibido o erro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19677344070423)

**Caso apresente erro, entrar em contato com o suporte para validação.**

How To com orientações de como realizar o ajuste:<https://www.youtube.com/watch?v=IJRr2gXQykY>

**4º Opção de gerar o arquivo TXT pelo extrator**

Gerar o arquivo TXT através do extrator fiscal

![Gravar_2024_06_26_11_37_14_708.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24446334078487)

E importar o TXT pela rotina Importação de arquivos (TAFA500)

![Gravar_2024_06_26_11_33_49_926.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24446349798679)

**Saiba mais:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Código da receita no TAF diferente do código da receita da Nota](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18664117621143-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-C%C3%B3digo-da-receita-no-TAF-diferente-do-c%C3%B3digo-da-receita-da-Nota?source=search)

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751)
