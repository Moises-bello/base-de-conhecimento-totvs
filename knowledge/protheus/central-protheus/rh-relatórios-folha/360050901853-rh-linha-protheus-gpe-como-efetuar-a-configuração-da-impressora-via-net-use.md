---
article_id: 360050901853
category: RH - Relatórios Folha
content_hash: 5a6e0d14de9aabe600a10bd5ec2d893542be467540f72bf470ace35b6c320219
fetched_at: '2026-06-28T22:43:17.454963+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar a configuração da impressora via NET
  USE
type: support-article
updated_at: '2024-09-18T20:36:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050901853-RH-Linha-Protheus-GPE-Como-efetuar-a-configura%C3%A7%C3%A3o-da-impressora-via-NET-USE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26468610023063) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como efetuar a configuração da impressora via NET USE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

1. Instale a impressora e seus drivers na estação de trabalho.  
2. Compartilhe a impressora na rede.  
3. No servidor, instale a impressora da estação que foi compartilhada na rede.

4. Mapeie, via **CMD.exe**, a impressora na porta **LPT\*** utilizando o comando: **NET USE LPT\* \\NOME\_ESTACAO\IMPRESSORA**

'\*' Esta é a porta que irá mapear: **LPT1, LPT2**,...

5. Acesse a rotina Local de Impressão (**ACDA060**), e inclua um local de impressão com a seguinte configuração:

**Código** = Informe o código desejado.  
**Descrição** = Informe a descrição desejada.  
**Modelo** = DATAMAX.  
**Porta Serial** = Nenhum.  
**Settings** = Deixe em branco.  
**Porta LPT** = Informe a porta **LPT** mapeada no **NET USE**.  
**Tipo** = Servidor.  
**Ver. Status** = Não.  
**Drv. Windows** = Não.

6. Após estes passos, configure corretamente os parâmetros **MV\_IACD01, MV\_IACD02, MV\_IACD03** e **MV\_IACD04** com o nome das respectivas impressoras.

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
