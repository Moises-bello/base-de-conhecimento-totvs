---
article_id: 40240017042455
category: Comércio Exterior - Easy Import Control - Portal Único
content_hash: 0b53b94d0f35c32baa03da81da778fe638766b773e403e9b89ecf052107f47cf
fetched_at: '2026-06-28T22:39:40.288976+00:00'
product: protheus
section_id: 27387892471703
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - A rotina de
  itens da DUIMP não está atualizada com a última expedição continua.
type: support-article
updated_at: '2026-05-07T17:49:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40240017042455-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-A-rotina-de-itens-da-DUIMP-n%C3%A3o-est%C3%A1-atualizada-com-a-%C3%BAltima-expedi%C3%A7%C3%A3o-continua
---

A mensagem "A rotina de itens da DUIMP não está atualizada com a última expedição contínua" ocorre quando o dicionário de dados da rotina EICDI502 está desatualizado. Para corrigir, é necessário baixar e aplicar o pacote de Expedição Contínua do SIGAEIC, garantir o arquivo sdfbra.hlp na pasta Systemload, executar o utilitário UPDDISTR e validar a atualização no módulo Easy Import Control.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40240024075543) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como corrigir a mensagem ' A rotina de itens da DUIMP não está atualizada com a última expedição continua'?  
![Erro_EIC.png](https://totvssuporte.zendesk.com/attachments/token/BBhud8qnve9mA9Cz15WlWnUEW/?name=Erro_EIC.png&lotus_request=true)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control (SIGAEIC) - A partir da versão 12.1.33

**Solução**  
Este incidente ocorre quando a rotina de **Itens da DUIMP (EICDI550)** está operando com um dicionário de dados (campos, telas e tabelas) desatualizado em relação aos binários e pacotes de funções do sistema. Para regularizar a interface e as funcionalidades da DUIMP, é mandatória a aplicação do pacote de expedição contínua e a atualização do dicionário via UPDDISTR.

**Passos**

1. Realize o download do pacote de **Expedição Contínua do módulo SIGAEIC** no Portal do Cliente;
2. Aplique o pacote de atualização (patch) em seu ambiente de homologação primeiramente;
3. Certifique-se de que o arquivo de dicionário diferencial (`sdfbra.hlp`) esteja na pasta **Systemload** (ou na estrutura definida no seu `appserver.ini`);
4. Execute o utilitário **UPDDISTR** para que as alterações de campos, índices e gatilhos específicos da DUIMP sejam processadas na base de dados;
5. Após a conclusão com sucesso, acesse o módulo **Easy Import Control (SIGAEIC)**;
6. Vá em **Atualizações** > **Desembaraço** > **Itens DUIMP** e valide se a rotina foi atualizada.

**Saiba mais**

[**Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Pacote-Acumulado-Comex)

[**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Procedimento UPDDISTR**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005365602-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Procedimento-UPDDISTR)

[**Atualizador de dicionário e base de dados - UPDDISTR**](https://tdn.totvs.com/pages/releaseview.action?pageId=181965468)
