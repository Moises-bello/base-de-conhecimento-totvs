---
article_id: 1500008406942
category: TAF - REINF
content_hash: 3f84fc7b96f2a0ddf709848e07f07a76f1a94f2f0cd489edd6c86ac3975d6b33
fetched_at: '2026-06-28T22:41:33.605074+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - Aquisição de produção
  rural '
type: support-article
updated_at: '2023-03-31T16:54:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008406942-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Aquisi%C3%A7%C3%A3o-de-produ%C3%A7%C3%A3o-rural
---

**Dúvida**Como Gerar o evento R-2055 - Aquisição de produção rural   
  
**Ambiente**A partir da versão 12.1.17  
  
**Solução**

1) Para que seja Transmitido o evento R-2055, você precisa estar com a ultima atualização do TAF/Reinf, Lib e com o Painel Reinf Configurado.

* Atualização Reinf: [TAF - REINF - Atualização completa Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-TAF-REINF-Atualiza%C3%A7%C3%A3o-completa-Reinf?source=search)
* Configuração Painel Reinf: [TAF - REINF - Configuração Painel Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004213201-TAF-REINF-Configura%C3%A7%C3%A3o-Painel-Reinf?source=search)

2) A nota precisa estar configurada conforme a documentação do Fiscal.

1. [MP - FIS - Como parametrizar pessoa física na entrada da nota fiscal?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024021132-MP-FIS-Como-parametrizar-pessoa-f%C3%ADsica-na-entrada-da-nota-fiscal-?source=search)

3) Para habilitar o preenchimento do campo A2\_CPFRUR.

* [MP - FIS - Solucionar mensagem CPF Rural / Valor inválido (CPF Rural) ao preenche o campo A2\_CPFRUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001834761-MP-FIS-Solucionar-mensagem-CPF-Rural-Valor-inv%C3%A1lido-CPF-Rural-ao-preenche-o-campo-A2-CPFRUR?source=search)

4) Configuração para o enquadramento da lei 13.606/2018

* [TAF - CONFIGURAÇÕES PARA O ENQUADRAMENTO DA LEI 13.606/2018 S-1250, R-2055](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027276172-TAF-CONFIGURA%C3%87%C3%95ES-PARA-O-ENQUADRAMENTO-DA-LEI-13-606-2018-S-1250-R-2055?source=search)

5) FUNRURAL - Fundo de Assistência ao Trabalhador Rural.

* <https://tdn.totvs.com/display/public/PROT/FIS0111+-+SENAR+%2C+INSS+E+GILRAT>

6) Após Configuração da nota deve ser executado o Extrator fiscal.

* Filtrar Reinf deve ser = **Sim.**
* Documentação extrator fiscal: [TAF - REINF - Extrator Fiscal - Detalhamentos dos Layouts](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023075011-TAF-REINF-Extrator-Fiscal-Detalhamentos-dos-Layouts?source=search)

OBS: Antes de gerar o Extrator fiscal, verifique o conteúdo do parâmetro **MV\_TAFRND**. Esse parâmetro é responsável por arredondar ou truncar o valor do imposto na nota que será levada para o TAF. **1 - Arredonda** ou **2 - Trunca.**

7) Após a execução do extrator fiscal deve ser avaliado o gerenciador de integração.

* [TAF - REINF - Gerenciador de integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043361753-TAF-REINF-Gerenciador-de-integra%C3%A7%C3%A3o?source=search).

8) para transmissão dos eventos, deve seguir a documentações.

* <https://tdn.totvs.com/display/TAF/Painel+REINF>
* <https://tdn.totvs.com/display/public/TAF/EFD-Reinf>

Para informar a conta contábil manualmente no TAF  preencha o campo (C30\_CODCTA) - Conta Contábil  no documento fiscal.
