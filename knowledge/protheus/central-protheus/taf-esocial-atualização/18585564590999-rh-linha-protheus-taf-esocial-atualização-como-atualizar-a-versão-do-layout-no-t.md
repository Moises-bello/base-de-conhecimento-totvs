---
article_id: 18585564590999
category: TAF - eSocial - Atualização
content_hash: 04b3d8fd618ade90638fe79bb3330caf84b572fe897ae540a48c518c597ed67e
fetched_at: '2026-06-28T22:45:13.310453+00:00'
product: protheus
section_id: 1500001547902
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Como atualizar a versão
  do layout no TAF E-social?
type: support-article
updated_at: '2025-01-30T18:18:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18585564590999-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Como-atualizar-a-vers%C3%A3o-do-layout-no-TAF-E-social
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18585578147351) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**RH - Linha Protheus - TAF - eSocial - Atualização - Como atualizar a versão do layout no TAF E-social?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus, RM, Datasul) - eSocial - TAF eSocial - Atualização - Todas as versões

**Solução em vídeo:**

**\*\* Vídeo ilustrativo, layout do eSocial deve ser alterado para versão S-1.3 (S\_01\_03\_00) á partir de 02/12/2024;**

**Solução (leitura):**

⚠ **Para realizar a atualização do layout no TAF é necessário que você faça as atualizações relacionadas abaixo:**

**[Atualização do seu ambiente TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-Automa%C3%A7%C3%A3o-Fiscal-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-)**

**[Atualização do seu ambiente do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7658806742679).** 

1. Para atualizar o layout do TAF E-social, acesse o módulo 84 e acesse as seguintes opções no menu do TAF:

```
Atualizações ➤ Configs. TAF ➤ Parâmetros.
```

![Menu.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18585564533911)

2. Acessando os parâmetros do sistema, pesquise em "Informações" o parâmetro abaixo responsável pelo layout do E-Social

```
MV_TAFVLES
```

3. Após a pesquisa do parâmetro MV\_TAFVLES, clique no botão "Alterar" e insira no campo "Conteúdo" o valor correspondente ao **layout 1.3 (S\_01\_03\_00).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28043119394711)

4. Depois do preenchimento do conteúdo clique em "Confirmar" e depois em "Sim" para salvar as alterações feitas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28043119396375)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28043104032023)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28043104032919)

**Versões do Layout:**

|  |  |
| --- | --- |
| **Layout:** | **Conteúdo para o parâmetro:** |
| 1.3 | S\_01\_03\_00 |
| 1.2 | S\_01\_02\_00 |
| 1.1 | S\_01\_01\_00 |
| 1.0 | S\_01\_00\_00 |
| 2.5 | S\_02\_05\_00 |
| 2.4.2 | S\_02\_04\_02 |
| 2.4.1 | S\_02\_04\_01 |

Pronto, seu Layout está atualizado !

Você pode validar se realmente foi atualizado acessando a [tela de diagnóstico do TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-Automa%C3%A7%C3%A3o-Fiscal-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF).

**\* Datas eSocial para a versão de layout S-1.3:**

* Implantação no ambiente produção - 02/12/2024
* Convivência v. S-1.2 com v. S-1.3 - até 02/02/2025

[Documentação do eSocial - Publicação da Versão S-1.3 dos Leiautes do eSocial e da Nota Técnica nº 04/2024 Revisada](https://www.gov.br/esocial/pt-br/noticias/publicacao-da-versao-s-1-3-dos-leiautes-do-esocial-e-da-nota-tecnica-no-04-2024-revisada)

**Documentos relacionados:**

[RH - Linha Protheus - GPE - eSocial - Como se adequar ao leiaute S-1.3 eSocial e para quais releases está disponível as atualizações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26092480826007-RH-Linha-Protheus-GPE-eSocial-Como-se-adequar-ao-leiaute-S-1-3-eSocial-e-para-quais-releases-est%C3%A1-dispon%C3%ADvel-as-atualiza%C3%A7%C3%B5es#:~:text=D%C3%BAvida-,Como%20se%20adequar%20ao%20leiaute%20S%2D1.3%20eSocial%20e%20para,releases%20est%C3%A1%20dispon%C3%ADvel%20as%20atualiza%C3%A7%C3%B5es%3F&text=Para%20preparar%20o%20seu%20ambiente,inclusive%20as%20atualiza%C3%A7%C3%B5es%20de%20dicion%C3%A1rios)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
