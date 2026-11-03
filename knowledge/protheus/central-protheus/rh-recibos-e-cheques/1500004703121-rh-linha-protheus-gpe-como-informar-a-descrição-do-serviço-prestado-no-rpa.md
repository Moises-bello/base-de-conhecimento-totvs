---
article_id: 1500004703121
category: RH - Recibos e Cheques
content_hash: 20dc216dd9e1773afff75d010b3c28580e750c8ddd2cd3194a8809b9c33e62c8
fetched_at: '2026-06-28T22:43:29.522010+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Como informar a descrição do serviço prestado no
  RPA
type: support-article
updated_at: '2022-11-11T21:32:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004703121-RH-Linha-Protheus-GPE-Como-informar-a-descri%C3%A7%C3%A3o-do-servi%C3%A7o-prestado-no-RPA
---

**Dúvida**Como informar a descrição do serviço prestado no RPA - Recibo de Pagamento Autônomo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Verificando o *rdmake* IMPRPA é possível identificar que o programa busca as informações de prestação de serviços do campo **Tp. Serv. Aut(RA\_SERVICO)** da Rotina **Contribuinte Individual - GPEA265  
![](https://totvssuporte.zendesk.com/attachments/token/2LzjmT0ELVVLTQC26pgvpbGEs/?name=inline1311693890.png)**

Para solução execute os procedimentos relacionados abaixo:  
  
1- Verifique se o campo Tp. Serv. Aut esta flegado como Usado no Dicionário de Dados.  
Acesse no Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SRA ->Campo RA\_SERVICO / Aba Uso flegar o item **Usado**: **![](https://totvssuporte.zendesk.com/attachments/token/9xpxgnGYeuHHfa2h1nduOLt3L/?name=inline-813872698.png)**2 - Em **Gestão de Pessoal - SIGAGPE**, você deve acessar a rotina **Contribuinte Individual**, selecionar a matrícula, e incluir a informação de Prestação de Serviço no campo **Tp. Serv. Aut** localizado na aba **Outras Informações  
![](https://totvssuporte.zendesk.com/attachments/token/MGsP7ECGAWk3azqxynHrtasMH/?name=inline-1221766935.png)**Executando os procedimentos acima, ao imprimir o Recibo de Pagamento de Autônomo a informação de prestação de serviço será carregada: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006312142/mceclip0.png)​  
  
​  
​**
