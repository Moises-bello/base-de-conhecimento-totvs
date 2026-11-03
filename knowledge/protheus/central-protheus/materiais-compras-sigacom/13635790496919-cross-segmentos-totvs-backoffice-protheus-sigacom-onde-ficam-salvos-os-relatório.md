---
article_id: 13635790496919
category: Materiais - Compras (SIGACOM)
content_hash: 40bc2740edc9a2724876e65d9bab97f9021ff3ace65b6023168c9e897bd683dc
fetched_at: '2026-06-28T22:41:22.030116+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Onde ficam Salvos os
  Relatórios personalizados dentro do Protheus?
type: support-article
updated_at: '2023-04-06T11:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13635790496919-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Onde-ficam-Salvos-os-Relat%C3%B3rios-personalizados-dentro-do-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Onde ficam salvos os Relatórios Personalizados dentro do Protheus?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - A partir da versão 12.1.25  
  
**Solução**

Foi criado um programa para forçar a reimportação de conteúdo do arquivo de leiautes, que só foi possível devido a natureza isolada do conteúdo do arquivo treport.spf.

Os dados na tabela de leiautes no banco de dados serão excluídos e os dados existentes no arquivo /profile/treport.spf serão importados para a tabela no banco de dados.

A funcionalidade está disponível a partir da **lib 20200214** e depois de ter esta lib ou superior aplicada no ambiente execute os passos a seguir. Adicione a opção "**Reimportação de Leiautes Treport**" no menu Configurador - programa: **APCFGLAYTR** ou utilize o menu atualizado na expedição da release 27 (opção disponível em **Ambiente / Cadastros / Reimportação de Leiautes TReport**); Coloque o arquivo **treport.spf** que possui os seus leiautes para reimportação na pasta **/profile/**; Acione o programa de reimportação no menu (menu padrão fica em **Ambiente / Cadastros / Reimportação de Leiautes TReport**) ; Leia as informações e confirme as perguntas para o processamento ; Acesse os relatórios conhecidos e verifique que os leiautes foram importados corretamente.

Saiba mais:

* [Sistema no Banco de Dados / Reimportação de leiautes de relatórios](https://tdn.totvs.com/pages/releaseview.action?pageId=532047103)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fontes de Relatórios de Compras para personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022534771-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Fontes-de-Relat%C3%B3rios-de-Compras-para-personaliza%C3%A7%C3%A3o?source=search)

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
