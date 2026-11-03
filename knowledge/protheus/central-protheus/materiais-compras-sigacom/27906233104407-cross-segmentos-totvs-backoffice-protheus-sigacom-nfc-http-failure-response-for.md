---
article_id: 27906233104407
category: Materiais - Compras (SIGACOM)
content_hash: f6b61ff9be50fd6e929aed1365414e040798b533c23e3897bae7c47496f0b62c
fetched_at: '2026-06-28T22:41:21.819832+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Http failure
  response for http://linknfc 500 Internal Server Error ao analisar cotação
type: support-article
updated_at: '2026-06-10T18:26:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27906233104407-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Http-failure-response-for-http-linknfc-500-Internal-Server-Error-ao-analisar-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27906233087639) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Ao analisar cotação no Novo Fluxo de Compras, sistema gera erro Http failure response for http://linknfc 500 Internal Server Error. Como corrigir?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - A Partir da versão 12.1.2310

**Solução**

Seguir o passo a passo descrito abaixo:

**1º passo:** Realize teste em ambiente de Homologação com as atualizações a seguir:

- [Acumulado Compras conforme sua versão](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

- LIB Atual -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168735)

- Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1112221) | [Onca](https://suporte.totvs.com/portal/p/10098/download?e=1168455)

Observação.: Aplicar após backups e validar primeiro em ambiente teste.

Caso o comportamento não seja resolvido execute o passo 2.

**2º passo:**Renomeie a pasta **HTTP\_ROOT** que fica dentro do diretório **Protheus\_Data**. Após isso reinicie os serviços do APPSERVER e realize novo teste.

**3º passo:** Adicione as chaves abaixo no appserver.ini do serviço Protheus:

[General]  
rest\_log\_level=4

[Sessão Ambiente]  
tracestack=1

Observação.: Renomeie o console.log, execute o processo novamente na rotina NFC e nos encaminhe para analise.

**4º passo:** Se porventura, o comportamento ocorrer no momento de enviar o email para o fornecedor pedimos que realize o processo abaixo:  
  
Realizar um teste usando a documentação e valide se irá ser gerado algum erro durante a execução da rotina: <https://tdn.totvs.com/display/PROT/WFTEST>  
Se for apresentado algum error.log, nos encaminhe para analise.

**5º passo:** Caso venha aparecer o erro "Internal Server Error" com a mensagem informando que o email não está configurado, revise configuração dos parâmetros abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27906652912791)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Parâmetros e Tabelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20433834878103-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Par%C3%A2metros-e-Tabelas)

**6º passo:** O erro ***500 internal server error*** também pode ser gerado caso o arquivo HTML esteja desatualizado. Portanto, é fundamental que baixe a versão atualizada e realize novos testes incluindo novas cotações.

Para realizar o download é necessário acessar a documentação abaixo e seguir o caminho destacado:

[Novo Fluxo de Compras: Guia de Referência - Gestão de Compras - P12](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500#NovoFluxodeCompras:GuiadeRefer%C3%AAnciaGest%C3%A3odeComprasP12-04.CONFIGURA%C3%87%C3%95ES:~:text=PR%C3%89%2DREQUISITOS%20M%C3%8DNIMOS-,04.%20CONFIGURA%C3%87%C3%95ES,-05.%20NOTAS%20DE)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41123547984279)

**Saiba Mais:**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
