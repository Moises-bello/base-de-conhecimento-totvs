---
article_id: 40406788369559
category: Gestão de Transportes (TMS)
content_hash: d5973be5be86b1461cc3e81af65f661b281ba601f2192fbdf3e0aa3ce4a66ed5
fetched_at: '2026-06-28T22:45:27.269164+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Averbação de CTe Ramo 59 RCV na AT&M
type: support-article
updated_at: '2026-05-12T13:56:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40406788369559-Log%C3%ADstica-Linha-Protheus-TMS-Averba%C3%A7%C3%A3o-de-CTe-Ramo-59-RCV-na-AT-M
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40406783301783) Tempo aproximado para leitura: **00:02:35 min**  
  
**Dúvida**  
Como adequar o **XML** do **CTe** para realizar a averbação no **ramo 59 - RCV** na **AT&M**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
A **AT&M** disponibilizou a seus clientes um manual orientando os ajustes técnicos necessários para adequação do **XML** dos documentos ao novo modelo de classificação de tipo de transportador para averbação no **ramo 59 - RCV**.  
  
A averbação de **RCV** é feito principalmente pelo **MDFe**, onde está especificado por padrão o veículo e transportador que está realizando o transporte. Conforme o manual técnico indica, para o **MDFe** não é necessário nenhum ajuste, pois já existe a *tag* nativa **<tpTransp> - Tipo do Transportador.**  
  
Visando atender a todos os clientes, em casos de transportes que não emitam MDFe para cobrir o transporte, a **AT&M** orienta substituir a tag adicional **AUTONOMO** pela nova tag adicional **TIPO\_TRANSPORTE**, na tag **<obsCont> - Observações do Contribuinte** no **XML** do **CTe**.  
O envio dessa *tag* só é necessário para casos de transporte sem **MDFe**, a depender da configuração da apólice e da seguradora.  
  
A **AT&M** também informou que **CTes** sem a informação de **TIPO\_TRANSPORTE** só terão a averbação rejeitada caso a apólice do **ramo 59 - RCV** esteja configurada para averbar no **CTe**.   
  
Por tratar-se de uma *tag* adicional, que é uma *tag* de uso livre do contribuinte, o **TMS** não realiza a montagem dessa informação no **XML**. Recomendo que avalie com sua seguradora se sua apólice do **ramo 59 - RCV** está configurada para averbar pelo **MDFe** ou **CTe**.  
  
Caso sua apólice esteja configurada para averbar pelo **CTE** e tenham alguma operação de transporte que não seja averbada pelo **MDFe**, para averbar o **RCV** pelo **CTe**, terão que customizar a montagem do **XML** diretamente no rdmake **CTESEFAZ3**, preenchendo os dados necessários conforme manual da **AT&M** e manual da **SEFAZ**. O rdmake mais recente está disponível em anexo a documentação [**Logística - Linha Protheus - TMS - RDMAKES para o CTe e MDFe**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/24339487959703-Log%C3%ADstica-Linha-Protheus-TMS-RDMAKES-para-o-CTe-e-MDFe)**.**  
  
**Glossário**  
**CTe** - Conhecimento de Transporte eletrônico  
**MDFe** - Manifesto de Documentos Fiscais eletrônico  
**RCV** - Responsabilidade Civil do Veículo  
**SEFAZ** - Secretaria da Fazenda  
**XML** - Extensible Markup Language  
  
**Anexo**
