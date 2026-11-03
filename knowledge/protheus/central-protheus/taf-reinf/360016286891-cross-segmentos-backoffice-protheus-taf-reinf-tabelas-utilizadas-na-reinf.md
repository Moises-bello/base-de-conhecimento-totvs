---
article_id: 360016286891
category: TAF - REINF
content_hash: 5debccc4426fd28bd22271dbceab17eda69e78caba8cfe0155c639bce200c2d8
fetched_at: '2026-06-28T22:41:34.872222+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Tabelas utilizadas na
  Reinf
type: support-article
updated_at: '2023-04-04T12:06:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016286891-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Tabelas-utilizadas-na-Reinf
---

**Dúvida**

Quais tabelas são utilizadas na Reinf?

**Solução**

Apuração dos Eventos

* R-2030
* R-2040
* R-2050
* R-2055
* R-2060
* R-2098
* R-2099
* R-3010
* R-5001

### **Evento R-1000 → Informações do Contribuinte**

**T9U - Informação do Contribuinte**

### **Evento R-1070 → Tabela de Processos Administrativos/Judiciais**

O cadastro para o evento R-1070 → Tabela de Processos Administrativos/Judiciais armazena os dados de origem do cadastro de [Informações de Processos](http://tdn.totvs.com/display/public/TAF/EFD-Reinf#EFD-Reinf-Informa%C3%A7%C3%B5esdeProcessos).

Pode ser acessado através do menu Eventos REINF **→ Tabelas → R-1070 - Processo Referenciado** pelo programa TAFA495, onde são utilizadas as seguinte tabelas:

* T9V - Tab. Processos Adm/Judiciais
* T9X - Informações de Suspensão

### 

### **Evento R-2010 → Retenção Contribuição Previdenciária - Serviços Tomados**

O cadastro para o evento R-2010 → Retenção Contribuição Previdenciária - Serviços Tomados e consolida os dados apurados com origem nos seguintes cadastros:

* Estabelecimento
* Cadastro de Obras
* Participante
* Documento de Entrada
* Fatura
* Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2010 - Retenção Cont. Previd. Serviços Tomado** pelo programa TAFA486, onde são utilizadas as seguinte tabelas:

* T95 - Ret. Contrib Prev - Serv Tomado
* T96 - Detalhamento de NFS
* T97 - Tipos de Serviços NF
* T98 - Inf. Processos Relacionados
* T99 - Inf. Processos Relacionados Ad
* C20 - Capa do Documento Fiscal
* C30 - Itens do Documento Fiscal
* C35 - Trib Itens Documento Fiscal
* LEM - Cadastro de Recibo/Fatura
* T5M - Tipo de Serviço
* C1H - Participantes

### **Evento R-2020 → Retenção Contribuição Previdenciária - Serviços Prestados**

O cadastro para o evento R-2020 → Retenção Contribuição Previdenciária - Serviços Prestados e consolida os dados apurados com origem nos seguintes cadastros:

* Estabelecimento
* Cadastro de Obras
* Documento de Saída
* Fatura
* Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2020 - Contr. Previd. - Serviços Prestados** pelo programa TAFA478, onde são utilizadas as seguinte tabelas:

* CMN - Ret. Contrib Prev - Serv Prest
* CRO - Detalhamento de NFS
* T9Y - Tipos de Serviços NF
* T9Z - Inf. Processos Relacionados
* V0A - Inf. Processos Relacionados Ad
* C20 - Capa do Documento Fiscal
* C30 - Itens do Documento Fiscal
* C35 - Trib Itens Documento Fiscal
* LEM - Cadastro de Recibo/Fatura
* T5M - Tipo de Serviço
* C1H - Participantes

### **Evento R-2030 → Recursos Recebidos por Associação Desportiva**

O cadastro para o evento R-2030 → Recursos Recebidos por Associação Desportiva e consolida os dados apurados com origem nos seguintes cadastros:

* + Estabelecimento
  + Participante
  + Documenta de Saída
  + Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2030 - Recursos Rec. Por Associação Desportiva** pelo programa TAFA255, onde são utilizadas as seguinte tabelas:

* C9B - Recursos Receb Associação Desp
* V1G - Recursos Recebidos
* V1H - Det. Recursos Recebidos
* V1I - Processos Adm/jud
* C20 - Capa do Documento Fiscal
* C30 - Itens do Documento Fiscal
* C35 - Trib Itens Documento Fiscal
* LEM - Cadastro de Recibo/Fatura
* T5M - Tipo de Serviço
* C1H - Participantes

### 

### **Evento R-2040 → Recursos Repassados para Associação Desportiva**

O cadastro para o evento R-2040 → Recursos Repassados por Associação Desportiva e consolida os dados apurados com origem nos seguintes cadastros:

* + Estabelecimento
  + Participante
  + Documenta de Entrada
  + Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2040 - Recursos Rep. Por Associação Despo** pelo programa TAFA491, onde são utilizadas as seguinte tabelas:

* T9K - Recursos Rep Associação Desp
* V1J - Recursos Recebidos
* V1K - Det. Recursos Repassados
* V1L - Processos Adm/jud
* C20 - Capa do Documento Fiscal
* C30 - Itens do Documento Fiscal
* C35 - Trib Itens Documento Fiscal
* LEM - Cadastro de Recibo/Fatura
* T5M - Tipo de Serviço
* C1H - Participantes

### 

### **Evento R-2050 → Comercialização da Produção por Produtor Rural PJ/Agroindústria**

 O cadastro para o evento R-2050 → Comercialização da Produção por Produtor Rural PJ/Agroindústria e consolida os dados apurados com origem nos seguintes cadastros:

* Estabelecimento
* Participante
* Documenta de Saída
* Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2050 - Comercialização da Produção por Produtor Rural PJ/Agroindústria** pelo programa TAFA492, onde são utilizadas as seguintes tabelas:

* C35 – Trib. Itens Documentos Fiscais
* V1D – Comerc. Produção Produtor Rural
* V1E – Tipo de Comercialização
* V1F – Processos Administrativos/Judiciais
* C20 - Capa do Documento Fiscal
* C30 - Itens do Documento Fiscal
* C1H - Participantes

### **Evento R-2055→ Aquisição de Produtor Rural**

O cadastro para o evento R-2055 → Aquisição de Produtor Rural e consolida os dados apurados com origem nos seguintes cadastros:

* Estabelecimento
* Participante
* Documenta de Entrada
* Informações de Processos

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2055 - Aquisição de Produtor Rural** pelo programa TAFA576, onde são utilizadas as seguintes tabelas:

* V5S – Aquisição de Produção Rural
* V5T – Detalhes Aquisição Prod Rural
* V5U – Inf.Processos Aquis.Prod.Rural
* V5V – Detalhes NFs Aquisição Rural

### 

### **Evento R-2060 → Contribuição Previdenciária sobre a Receita Bruta - CPRB**

 O cadastro para o evento R-2060 → Contribuição Previdenciária sobre a Receita Bruta - CPRB consolida os dados apurados com origem nos seguintes cadastros:

* Contrib Prev Receita Bruta (cadastro legado origem TAFA097)

Pode ser acessado através do menu Eventos REINF **→ Periódicos → R-2060 - Cprb Contr. Previdênciária Receita Bruta** pelo programa TAFA499, onde são utilizadas as seguinte tabelas:

* V0S - Contribuição Prev. Recei. Bruta
* V0T - Registro Estabelecimento R2060
* V0U - R-2060 Ajustes Contrib. Apurad
* V0V - R-2060 Processos Susp Cprb
* C5M - Contrib Prev Receita Bruta
* C5O - Processos Referenciados - CP
* T9T - Tipo de Ajuste

### **Evento R-2098 →** **Reabertura dos Eventos Periódicos**

* V1A - Reabertura Eventos Periódicos

### **Evento R-2099 → Fechamento dos Eventos Periódicos**

* V1O - Controle de Períodos REINF
* V0B - Fechamento periódicos

### **Evento R-3010 → Receita de Espetáculo Desportivo**

ode ser acessado através do menu Eventos REINF **→ Não Periódicos → R-3010 - Receita de Espetáculo Desportivo** pelo programa TAFA298, onde são utilizadas as seguintes tabelas:

* T9F - Receita de Espetáculo Desportivo
* T9J - Processos Judiciais
* T9G - Boletim Espetáculo Desportivo
* T9H - Receita de Ingressos
* T9I - Outras Receitas

### 

### **Evento R-5001 → Informações de Bases e Tributos por Evento**

O evento R-5001 apresenta o retorno do RET contendo as informações de bases e tributos para cada um dos eventos enviados.  
Estes dados são obtidos durante o monitoramento da transmissão dos eventos, quando estes foram transmitidos com sucesso, e armazenados nas tabelas correspondentes.

Os dados armazenados podem ser acessados através do menu Eventos REINF **→ Totalizadores → R-5001- Informações de Bases/Tributos por Eventos,**através do programa TAFA501, no qual são utilizadas as seguintes tabelas:

* V0W - Evento Totalização
* V0X  - Totalizador do evento R-2050
* V0Y  - Totalizador do evento R-2040
* V0Z  - Totalizador do evento R-2040

### 

### **Evento R-5011 → Informações de Bases e Tributos Consolidadas por Período de Apuração**

O evento R-5011 apresenta o retorno do RET contendo as informações de bases e tributos consolidadas por período de apuração.   
Estes dados são obtidos durante o monitoramento da transmissão do evento R-2099 - Fechamento dos Eventos Periódicos, quando este for transmitido com sucesso, e armazenados nas tabelas correspondentes.

Os dados armazenados podem ser acessados através do menu Eventos REINF **→ Totalizadores → R-5011 - Informações de Bases/Tributos Consolidado,**através do programa TAFA497, no qual são utilizadas as seguintes tabelas:

* V0C - Inf. Bases e Trib. consolidado
* V0E - Informações Consolidadas
* V0F - Totalizador Serviços Tomados
* V0G -Totalizador Serviços Prestados
* V0H - Totalizador Associações Desp
* V0I  - Totalizador Com. Produção
* V0J - Totalizador CPRB

Para maiores informações:

<http://tdn.totvs.com/display/TAF/EFD-Reinf>

<http://tdn.totvs.com/display/public/PROT/EFD-REINF>

<http://tdn.totvs.com/display/public/PROT/Eventos+Reinf#Eventos-831245312>

Encontre também,

Manual do TAF - <http://tdn.totvs.com/display/TAF/Manual+do+TAF>

Extrator Fiscal - <http://tdn.totvs.com/display/PROT/FIS0001_Extrator_Fiscal_x_TAF>

Gerenciador de Integração - <http://tdn.totvs.com/pages/viewpage.action?pageId=192086625>

EFD Reinf TAF - <http://tdn.totvs.com/display/public/TAF/EFD-Reinf>

EFD Reinf Protheus - <http://tdn.totvs.com/display/public/PROT/EFD-REINF>
