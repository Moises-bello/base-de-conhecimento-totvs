---
article_id: 360052709673
category: MDT - PCMSO
content_hash: f9163371599f4a098359627a7f537340241944bea23e0c7a9f2c1812e6130fd0
fetched_at: '2026-06-28T22:44:28.322516+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Aviso ao gerar resultado de exame O arquivo XXXXXXXXX.dotm
  não foi encontrado no servidor. Verifique o parâmetro MV_DIRACA
type: support-article
updated_at: '2025-09-03T12:58:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052709673-RH-Linha-Protheus-MDT-Aviso-ao-gerar-resultado-de-exame-O-arquivo-XXXXXXXXX-dotm-n%C3%A3o-foi-encontrado-no-servidor-Verifique-o-par%C3%A2metro-MV-DIRACA
---

**Ocorrência**Aviso ao gerar resultado de exame O arquivo **XXXXXXXXX.dotm** não foi encontrado no servidor. Verifique o parâmetro **MV\_DIRACA.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho -  Todas as versões  
  
**Causa**

* Não existe pasta (diretório) com os arquivos de Templates **.dot** ou **.dotm**;
* O caminho definido no configurador para os pasta (diretório) com os arquivos de Templates .dot ou .dotm está incorreto.

**Solução**  
Para ajustar, acesse o modulo configurador (SIGACFG) no caminho ambiente > cadastros > parâmetros. Busque o parâmetro **MV\_DIRACA** e veja se no caminho do diretório definido existe no sistema os arquivos de Templates **.dot** ou **.dotm**.  
  
**Observação:** 

* Caso não exista os arquivos com **templates** consulte o artigo: [MP - MDT - Onde encontrar os arquivos de Templates .dot ou .dotm para geração de relatórios no modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051951334);
* O diretório deve estar dentro da pasta **protheus\_data**;
* Por padrão o sistema busca na pasta \**samples**\ mas esse diretório pode ser alterado conforme exemplo abaixo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083044174)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083044814)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
