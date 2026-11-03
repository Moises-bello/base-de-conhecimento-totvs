---
article_id: 15660869032087
category: eSocial - Gerar XML/ Integração Evento
content_hash: 292f0c8efe144b216b3ce15c64ee6fbd7310a86d64e0e1565348766fe33ed553
fetched_at: '2026-06-28T22:47:12.242485+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao integrar S-2200 ou S-2205: Erro código 882:
  Tipo de dependente inválido. Ação Sugerida: o valor informado deve existir na Tabela
  de Tipos de Dependentes'
type: support-article
updated_at: '2025-07-02T17:56:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15660869032087-RH-RM-FOP-eSocial-Erro-ao-integrar-S-2200-ou-S-2205-Erro-c%C3%B3digo-882-Tipo-de-dependente-inv%C3%A1lido-A%C3%A7%C3%A3o-Sugerida-o-valor-informado-deve-existir-na-Tabela-de-Tipos-de-Dependentes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15660826374807) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao integrar com o governo o evento S-2200 ou S-2205 ocorre o **Erro código 882: Tipo de dependente inválido. Ação Sugerida: o valor informado deve existir na Tabela de Tipos de Dependentes.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15660411882519)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2205.248; 12.1.2209.197; 12.1.2302.121 e Superiores.

**Causa**A partir da Nota Técnica 01/2023 a Tabela 07 - Tipos de Dependente sofreu alteração, foi excluído o tipo **4 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau**. Assim, ao integrar um evento que o tpDep ainda como consta como 4 no XML, o governo acusa o erro.

**Solução**Foram realizados os ajustes no produto e ao preencher Grau de Parentesco 1 e Universitário/Escola Técnica 2° Grau o sistema fará o de/para automaticamente.   
1. Localize o funcionário com o erro e vá em**Anexos | Folha de Pagamento | Dependentes**.

![](https://tdn.totvs.com/download/attachments/745755598/image2023-3-21_9-31-35.png?version=1&modificationDate=1679401911927&api=v2)

2. Ao cadastrar com a parametrização abaixo o XML era gerado com o tipo 4 - Filho(a) ou enteado(a), universitário(a) ou cursando escola técnica de 2º grau, com a implementação da nota técnica passa a ser gerado com o **Tipo 3 - Filho(a) ou enteado(a)**.

![](https://tdn.totvs.com/download/attachments/745755598/image2023-3-24_8-23-22.png?version=1&modificationDate=1679657044567&api=v2)

3. DE/PARA.

![](https://tdn.totvs.com/download/attachments/745755598/image2023-3-24_8-36-11.png?version=1&modificationDate=1679657814543&api=v2)

![](https://tdn.totvs.com/download/attachments/745755598/image2023-3-24_8-33-40.png?version=1&modificationDate=1679657662967&api=v2)

**Importante**Após atualização da Versão e/ou Pacote faz-se necessário rodar o RM.Atualizador e Reiniciar o Host.

**Saiba mais**  
Para saber mais sobre estas e outras alterações da NT 01/2023, acesse:  
     [Nota Técnica nº 01/2023](https://tdn.totvs.com/pages/releaseview.action?pageId=745755598)
