---
article_id: 17155332287895
category: eSocial - Gerar XML/ Integração Evento
content_hash: 59c4b140fb0009e70b8e63b7c814fa211e3e8a58996a8af6918cf5b8bc702170
fetched_at: '2026-06-28T22:47:13.037099+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Geração do S-1200 e S-1210 para transportador autônomo
  externo
type: support-article
updated_at: '2024-06-28T12:36:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17155332287895-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1200-e-S-1210-para-transportador-aut%C3%B4nomo-externo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17155366067223)**Tempo aproximado para leitura: **00:02:30 min  
  
Dúvida:**  
Como gerar o evento S-1200 e S-1210 para transportador autônomos externos?

**Ambiente:**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões

**Solução**Conforme MOS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24499641657751)

Desta forma, siga os passos abaixo para realizar a correta geração dos eventos S-1200 e S-1210 no RM:

1. Execute o script **ESOCIALFOP01-10709.SQL** (para base SQL) ou **ESOCIALFOP01-10709.ORA** (para base ORACLE) através do aplicação **RM.Script.Executor.exe**;  
2. Preencha sua tabela **PPAGTOAUTONOMOEXT** conforme sua integração (*Webservice*, conceito, etc.) e valide os valores dos campos:  
2.1. **CATEGORIAESOCIAL**: **711** - Contribuinte individual - Transportador autônomo de passageiros ou **712** - Contribuinte individual - Transportador autônomo de carga;  
2.2. **VALORREMUNFRETEINCIDEINSS**: valor da remuneração correspondente à **base de INSS**;  
2.3. **VALORREMUNFRETEINCIDEIRRF**: valor da remuneração correspondente à **base de IRRF**;  
2.4. **VALORREMUNERACAOFRETE**: Valor **total** do frete. O sistema irá automaticamente subtrair os valores da base de INSS e IRRF no momento de gerar o XML;  
2.5. **VALORINSS**: valor do desconto de **INSS**;  
2.6. **VALORSEST**: valor do desconto correspondente ao **SEST**;  
2.7. **VALORSENAT**: valor do desconto correspondente ao **SENAT**;

3. Acesse **Configurações | Parametrizador | eSocial | Autônomos e Externos 1/2** e **Autônomos e Externos 2/2.** No parametrizador devem existir eventos previamente cadastrados para serem informados no eSocial.

![](https://tdn.totvs.com/download/attachments/496796713/image2019-3-6_17-2-19.png?version=1&modificationDate=1559771715517&api=v2)

![](https://tdn.totvs.com/download/attachments/496796713/image2019-3-6_17-2-39.png?version=1&modificationDate=1559771715567&api=v2)

3. Gerar o XML dos eventos periódicos S-1200 e S-1210 do período.

* S-1200 - Remuneração do Trabalhador

![](https://tdn.totvs.com/download/attachments/496796713/image2019-6-5_18-52-27.png?version=1&modificationDate=1559771712900&api=v2&effects=border-simple,shadow-kn)

* S-1210 - Pagamentos de Rendimentos

![](https://tdn.totvs.com/download/attachments/496796713/image2019-6-5_18-54-34.png?version=1&modificationDate=1559771712850&api=v2&effects=border-simple,shadow-kn)

**Saiba mais:**  
- [Eventos S-1200 e S-1210 - Transportador autônomo - Autônomos Externo](https://tdn.totvs.com/pages/releaseview.action?pageId=496796713)   
- [Autônomos e Externos 1/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719944)   
- [Autônomos e Externos 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=463823367)   
- [Layout Para Importação de Autônomos Externos (Versão 12.1)](https://tdn.totvs.com/pages/releaseview.action?pageId=543064647)  
- [Importação de Dados da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039126793-RH-RM-FOP-Importa%C3%A7%C3%A3o-de-Dados-da-Folha-de-Pagamento)
