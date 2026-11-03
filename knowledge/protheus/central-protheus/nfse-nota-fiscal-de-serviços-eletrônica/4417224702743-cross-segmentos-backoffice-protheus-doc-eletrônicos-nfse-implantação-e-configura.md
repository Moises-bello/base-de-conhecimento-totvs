---
article_id: 4417224702743
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: cb057db892223df01724d25fc5b0bdfcde628b77dab94311d15b77c066c1cfe1
fetched_at: '2026-06-28T22:39:57.505532+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Implantação
  e Configuração do AUTONFSE (via Schedule)
type: support-article
updated_at: '2026-03-05T16:48:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417224702743-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Implanta%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-do-AUTONFSE-via-Schedule
---

**Dúvida**  
Como realizar a configuração do AUTONFSE via Schedules?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões  
  
**Solução**  
O AUTONFSE via Schedule é uma melhoria liberada em relação à sua [antiga configuração (via JOBS),](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015833992-MP-NFSE-Implanta%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-do-AUTONFSE) o qual ainda é uma opção porém não orientamos a utilização desse modelo antigo por questões de performance e estabilidade.  
Primeiramente o ambiente do Protheus deverá estar contemplando essa melhoria, portanto, se certificar de atualiza-lo de acordo com sua release: [12.1.2410](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1171486) | [12.1.2510](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224039).  
  
Após isso deverá realizar o passo a passo abaixo de configuração, lembrando que é compatível com a antiga e nova interface dos schedules.  
  
**1.** **Realizar a inclusão manual do grupo de perguntas para o 'JOBAUTNFSE':**  
- Acesse Configurador (**SIGACFG**) > Dicionário > Base de Dados > Perguntas > Incluir.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417220289431)

- Deverá cadastrar as perguntas: "Série?", "Número de Threads?" e "Quantidade de NFS-e p/ Lote?", na mesma ordem, com o mesmo tipo, tamanho, formato e objeto para o correto funcionamento:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4848083378327)

*IMPORTANTE: Realizar o backup da SX1.*

**2. CONFIGURAÇÃO DO SCHEDULE**  
- Se for utilizado, deverá desabilitar o antigo JOBNFSE no Appserver.ini do Protheus para evitar concorrência ([Detalhes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015833992-MP-NFSE-Implanta%C3%A7%C3%A3o-e-Configura%C3%A7%C3%A3o-do-AUTONFSE));  
- Deverá ser configurado via Configurador (SIGACFG), no menu: Ambientes/Schedule/Schedule;  
- Deverá cadastrar um Agent e um Agendamento;  
- Após conclusão e a ativação do Agent/Agendamento, as rotinas dão início ao processamento dos documentos.  
- Se necessário gravar o log de processamento das rotinas, efetue a seguinte configuração no arquivo appserver.Ini do Protheus na seção com o nome do Environment/Ambiente: AUTONFSE\_DEBUG=1

**3. CRIANDO UM AGENT**  
- Acessar o Configurador (SIGACFG);  
- Menu Configurador > Ambiente > Schedule;  
- Em “Agent” realizar a inclusão de um cadastro;  
- Cadastrar com os dados do ambiente do Protheus que utilizará essa configuração, exemplo abaixo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417226812055)

**4. CRIANDO UM AGENDAMENTO**  
- Acessar o Configurador (SIGACFG);  
- Menu Configurador > Ambiente > Schedule;  
- Em “Agendamentos” realizar a inclusão de um cadastro.  
- No campo “Rotina” informar a(s) rotina(s) que deseja configurar.  
**AUTONFSETRANS -** Responsável pela transmissão das notas;  
**AUTONFSEMON -** Responsável pelo Monitoramento das notas (Transmissão e Cancelamento);  
**AUTONFSECANC -** Responsável pela transmissão do Cancelamento  
- Em “Parâmetros” deverá ser informado a série do documento, número de threads e número de RPS por lote, exemplo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417241030039)  
  
Um detalhe importante é verificar a 'Recorrência' do Agendamento, o qual pode ser configurado para sempre ativo ou programado:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417227116951)  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417241457175)

Feito isso, se certificar de que o agendamento está devidamente configurado e o Agent/Schedules ativos:  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417241539607)  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417241549719)  
  
Dessa maneira as notas serão processadas conforme configurado (Transmissão e/ou Monitoramento e/ou Cancelamento) de forma automática.  
  
Seguem documentações complementares:  
- <https://tdn.totvs.com/pages/viewpage.action?pageId=652217147>   
- <https://tdn.totvs.com/pages/viewpage.action?pageId=650506123>
