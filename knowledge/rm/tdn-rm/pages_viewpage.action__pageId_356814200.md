---
content_hash: e651a056ace7ea65d0e561528ba943c1b01ad2893d4c7ba79e8b85430b2026e0
fetched_at: '2026-06-29T00:08:57.898515+00:00'
page_id: '356814200'
product: rm
source: tdn-rm
title: RMFIS00006_Wizard de Configuração do TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=356814200
version: 4
---

# Wizard de Configuração do TSS

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1 |
| **Ocorrência:** | Wizard de Configuração do TSS |
| **Ambiente:** | TAF |
| **Passo a passo:** | No Wizard de configuração do TSS no TAF será parametrizada informações como:   * Se o ambiente será utilizado como Produção ou Homologação para a rotina REINF * Configuração da URL + Porta do TSS (Previamente instalado) * Configuração do Certificado digital     Segue abaixo detalhamento:  O Wizard de Configuração do TSS está disponível no menu:  TAF | Atualizações | Configs. Taf. Wizard de Config. TSS      Após acessar o menu acima será apresentado a seguinte tela:      Ao avançar será necessário informar a Url Totvs Service SOA. Esse campo refere-se a URL+ Porta do servidor TSS previamente instalado.  No campo Ambiente REINF informe se será utilizado dados de homologação ou produção. (Ambiente 1 - Produção ou Ambiente 2- Pre Produção - dados reais)      **\*\* Dica:** Para identificar a porta do TSS acesse o appserver.ini disponível na pasta totvssped onde o TSS e localize a chave "[localhost:8081]" que apresenta os dados da URL de Webservice de acordo com o servidor e a porta informada na instalação:      Certifique-se de que a Url + Porta está funcionando, para isso teste-a no navegador web.      Caso a URL não seja valida, ou o servidor esteja fora do ar, ou o campo Url Totvs Service SOA esteja em branco será exibido a mensagem abaixo:  *WSCERR044/Não foi possível POST : URL/SPEDCFGNFe.apw (10049: Can't assingn requested adress.) ADVPL WSDL Client 1.120703/TOTVS Série T Serviços MSSQL ...*      Se as informações acima estiverem corretas será exibido a tela de configuração do certificado digital, neste passo será necessário informar o tipo de certificado, diretório e senha do certificado. Todas as informações do Certificado digital de acordo com as especificações do modelo de sua empresa.      Caso as informações estejam corretas será exibido uma mensagem de confirmação conforme imagem abaixo:      Após a clicar em "Ok" será exibido a mensagem de encerramento das configurações. |
| **Observações:** |  |
