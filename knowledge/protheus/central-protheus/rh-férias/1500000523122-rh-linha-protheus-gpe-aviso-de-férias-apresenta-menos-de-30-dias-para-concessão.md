---
article_id: 1500000523122
category: RH - Férias
content_hash: 01cf64001b3d83fa61d281fd9a85e101c37bfbc04b09aa66e19b0316c7b0b500
fetched_at: '2026-06-28T22:43:57.964909+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Aviso de férias apresenta menos de 30 dias para
  concessão das férias
type: support-article
updated_at: '2025-09-02T18:06:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000523122-RH-Linha-Protheus-GPE-Aviso-de-f%C3%A9rias-apresenta-menos-de-30-dias-para-concess%C3%A3o-das-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31722545023767)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Impressão do aviso de férias apresenta menos de 30 dias para concessão das férias.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Devido a **MP n°927/2020**, a qual prevê que durante o estado de calamidade pública, o empregador informará ao empregado sobre a antecipação de suas férias com antecedência de, no mínimo, **quarenta e oito horas**, por escrito ou por meio eletrônico, com a indicação do período a ser gozado pelo empregado, foi criado parâmetro **MV\_AVISFER**.

Sua configuração indica o **número de dias** de aviso das férias quando **diferente do padrão** previsto na CLT (30 dias).  
  
**Solução**Para que a impressão do aviso volte a apresentar o padrão de 30 dias, é necessário deixar o parâmetro em **branco**ou informar **30** em seu conteúdo.

Para isso, siga os seguintes passos:  
1. Acesse ambiente **Configurador** (SIGACFG) com perfil de administrador do sistema;  
2. Selecione no menu **Ambiente > Cadastros > Parâmetros**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000568641)  
  
3. Faça uma busca através do ícone da lupa pelo parâmetro **MV\_AVISFER;**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099443114)**

4. Clique em **editar** e altere seu conteúdo para **vazio** ou **30** e clique em **salvar;**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101654173)**

**Saiba Mais**[RH - Linha Protheus - GPE - Emissão de aviso e recibo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4810789551639-RH-Linha-Protheus-GPE-Emiss%C3%A3o-de-aviso-e-recibo-de-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Como emitir o aviso de férias do funcionário 30 dias antes do gozo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049657874-RH-Linha-Protheus-GPE-Como-emitir-o-aviso-de-f%C3%A9rias-do-funcion%C3%A1rio-30-dias-antes-do-gozo?source=search)  
[RH - Linha Protheus - GPE - Dados Bancários do Funcionário não aparecem no aviso e recibo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059548553-RH-Linha-Protheus-GPE-Dados-Banc%C3%A1rios-do-Funcion%C3%A1rio-n%C3%A3o-aparecem-no-aviso-e-recibo-de-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Como realizar a impressão do Aviso/Recibo de férias com licença remunerada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051618133-RH-Linha-Protheus-GPE-Como-realizar-a-impress%C3%A3o-do-Aviso-Recibo-de-f%C3%A9rias-com-licen%C3%A7a-remunerada?source=search)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
