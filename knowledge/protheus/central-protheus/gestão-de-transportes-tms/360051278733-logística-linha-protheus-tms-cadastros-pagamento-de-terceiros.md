---
article_id: 360051278733
category: Gestão de Transportes (TMS)
content_hash: 53e986856ecce11a104d5805036aa92a96bdd208484d3ea940fc82a2b296f747
fetched_at: '2026-06-28T22:45:27.328283+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Cadastros Pagamento de Terceiros
type: support-article
updated_at: '2022-05-31T18:54:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051278733-Log%C3%ADstica-Linha-Protheus-TMS-Cadastros-Pagamento-de-Terceiros
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min****Dúvida**Quais os principais cadastros para o pagamento de terceiros no **SIGATMS – Gestão de Transportes**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**Os principais cadastros relacionados ao pagamento de terceiros no **SIGATMS**são:

* **Componentes:**Acesse o menu **Atualizações\Comercial\Componentes - TMSA030.**Os componentes de frete a pagar devem utilizar no campo **DT3\_TIPFAI -****Calc. Sobre,** a numeração a partir de **51**.
* **Configuração tabela de frete:**Acesse o menu **Atualizações\Comercial\Config. Tab. Frete - TMSA130.**Cadastro utilizado para definir os componentes que serão utilizados pela tabela de frete, e se o valor do componente fará parte do cálculo dos impostos.
* **Tabela de frete a pagar:**Acesse o menu **Atualizações\Terceiros\Tab. Frete a pagar - TMSA790.**Neste cadastro é possível definir os valores dos componentes dentro de um percurso.  
  No cálculo de frete a pagar, o Sistema considera sempre a origem da **Rota**. O destino será de acordo com o parâmetro **MV\_ULTDEST - Utiliza o último destino da coleta/entrega para cálculo de frete**, se estiver configurado como **Falso**, o destino será o mesmo local de origem, caso contrário pegará o último documento da sequência da viagem.
* **Tabela de carreteiro:**Acesse o menu **Atualizações\Terceiros\Tab. Carreteiros - TMSA520.**Cadastro utilizado para definir somente a descrição da tabela de carreteiro e sua vigência.
* **Tabela de carreteiro por rota:**Acesse o menu **Atualizações\Terceiros\Tab. Carret p/Rota - TMSA220.**Cadastro onde é realizado o vínculo da **Tabela de Carreteiro** com uma **Rota**. Neste vínculo é possível definir o valor que será pago ao prestador de serviço, de acordo com o tipo de veículo, tipo de frota dos reboques, tipo de cálculo e tipo de viagem.
* **Contrato fornecedor:**Acesse o menu **Atualizações\Terceiros\Contrato Fornec - TMSA800.**Cadastro onde são definidas as particularidades do contrato do prestador de serviço - **Terceiro** ou **Agregado**, como:   
    
  + **Vigência;**
  + **Tipo de Transporte;**
  + **Tipo de Veículo;**
  + **Serviços de Transportes Prestados;**
  + **Tabelas de Frete;**
  + **Tabelas Alternativas.**
