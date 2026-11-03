---
article_id: 360057237614
category: RH - Transferência
content_hash: 45d037bfc0b1305c13b355c8b1c96ed9494ce737cc540aee9ba3620879163cba
fetched_at: '2026-06-28T22:43:23.365888+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre
  Empresas/Filiais
type: support-article
updated_at: '2026-04-16T14:53:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33449727549335) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**  
Como funciona a **movimentação de tabelas** quando é realizada a **transferência**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão Pessoal - Todas as versões  
  
**Solução**  
Para a transferência de funcionários **entre empresas/filiais**, o sistema originalmente atualiza os arquivos SR do módulo Gestão de Pessoal, assim, ao realizar um processo de transferência, as movimentações abaixo são executadas.  
  
**Para fazer a transferência entre empresas/filiais de arquivos do módulo Ponto Eletrônico ou para que qualquer outro módulo seja atualizado é necessário a configuração do parâmetro MV\_ARQTRAN.**  
  
[**Funcionamento do parâmetro MV\_ARQTRAN**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-MP-PON-Funcionamento-do-par%C3%A2metro-MV-ARQTRAN?source=search)  
  
Tabelas que **sofrem** **movimentação** - QUADRO A:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796177512855)  
  
Tabelas que **não sofrem movimentação** -QUADRO B:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39796177514007)

Existem algumas particularidades que ocorrem neste processo a depender do tipo de transferência aplicado sobre o funcionário:

* **Transferência entre Empresas**  
  Todas as tabelas listadas no quadro A, caso existirem para a matrícula em questão, terão seu conteúdo **copiado e inseridos** na empresa Destino com dados da empresa Destino.  
    
  Ou seja, na empresa de Origem permanecem os registros anteriores à transferência e registros novos são incluídos na empresa de Destino.   
  Neste cenário arquivos marcados com ![(estrela)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/star_yellow.svg) no quadro A são **deletados**da empresa origem e registros novos são incluídos na empresa de Destino.  
  Itens marcados com ![(aviso)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/warning.svg) possui condições para movimentação dos dados  
  - RU0 =>Não movimenta os registros  
  - SRK => Movimento apenas registros com verbas de natureza diferente de 9253 (eConsignado - Crédito do Trabalhador)  
    
  *Transferência entre Filiais com CGC iguais (dentro do mesmo Grupo de Empresas)*  
  Na ocasião de transferência entre Grupo de Empresas e filiais que possuírem o mesmo código CNPJ entende-se que trata-se do mesmo estabelecimento e desta maneira todos os registros são deletados no Grupo de Empresa Origem.  
  Porém entendemos que essa configuração é indevida uma vez que os impactos são além da movimentação dos dados de transferência como também para o eSocial, no Dissídio, Informe de Rendimentos e inclusive em relatórios como no Relatório de Folha de Pagamento.  
  Nesta ocasião orientamos que o processo de mudança de estrutura de filial seja feito acompanhado por um consultor, onde deve ser avaliado o modo de acesso, estrutura de todos os eventos, regra de negócio validando a correta transmissão dos eventos antigos e novos eventos.  
    
  Verificar documentação [25205757 DRHROTPRT-25877 DT Transferência entre Grupos de Empresas para filial de mesmo CNPJ](https://tdn.totvs.com/pages/viewpage.action?pageId=1024352624)

* **Transferências entre Filiais com CGC diferentes (dentro do mesmo Grupo de Empresas)**  
  Todas as tabelas listadas no quadro A, caso existirem para a matrícula em questão, terão seu conteúdo copiado e inseridos na filial Destino com dados da filial Destino com exceção das tabelas:  
    
  => Histórico de Movimentos (SRD),  
  => Histórico Outros Benefícios (RIR).  
    
  Ou seja, na filial de Origem permanecem os registros anteriores à transferência e registros novos são incluídos na filial de Destino.  
  Neste cenário arquivos marcados com ![(estrela)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/star_yellow.svg) no quadro A são deletados da filial Origem e registros novos são incluídos na Filial de Destino.  
  Itens marcados com ![(aviso)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/warning.svg) possui condições para movimentação dos dados  
  - RU0 =>Não movimenta os registro  
  - SRK => Movimento apenas registros com verbas de natureza diferente de 9253 (eConsignado - Crédito do Trabalhador)

* **Transferência entre Filiais com CGC iguais**  
  Todas as tabelas listadas no quadro A, caso existirem para a matrícula em questão, possuirão seus registros originais *alterados* para a filial destino.  
    
  Ou seja, na filial de Origem os registros são atualizados com as informações da filial de Destino.  
  Itens marcados com ![(aviso)](https://tdn.totvs.com/s/5bn9pn/8804/xgjkrn/_/images/icons/emoticons/warning.svg) possui condições para movimentação dos dados  
  - RU0 =>Movimenta todos os registro  
  - SRK => Movimento todos os registros
* **Transferência de tabelas de movimento mensal**  
  A parte das particularidades citadas nos itens anteriores, na ocasião de transferência de tabelas cuja movimentação é mensal como por exemplo:  
    
  => Movimento do Período (SRC),  
  => Incidências (RGB),  
  => Cabeçalho de Férias (SRH),  
  => Cabeçalho de Rescisão (SRG),  
  => Itens de Férias e Rescisões (SRR),  
  => Movimento de Valores Futuros (SRK),  
  => Cálculo Outros Benefícios (RIQ) e  
  => *Lançamento de Ausências (SR8).*  
    
  Será exibida uma tela onde o usuário pode selecionar para qual período ativo da Empresa/Filial destino esses registros deverão ser levados.  
  Os arquivos  anteriores serão deletados e inseridos no período selecionado pelo usuário com exceção dos arquivos em *itálico*.
* **Transferência do dados do Funcionário (SRA)**  
  Durante o processo de transferência o registro de Origem é  atualizado com as informações abaixo:  
    
  => Situação Folha igual a D - Demitido (RA\_SITFOLH)  
  => Data de Demissão (RA\_DEMISSA)  
  => Cód. Resc. RAIS (RA\_RESCRAI) - 30/31 para transferência entre Empresas ou Filiais de CGC diferentes  
  => Cód. Afast. RAIS (RA\_AFASFGT) - N2 para transferência entre Empresas ou N1 para demais.  
  => Crachá (RA\_CRACHA)  
  **Um novo registro é admitido no Destino.**

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=540895964)  
[RH - Linha Protheus - GPE - Transferência de funcionário, vindo de outro Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413843598743-RH-Linha-Protheus-GPE-Transfer%C3%AAncia-de-funcion%C3%A1rio-vindo-de-outro-Sistema?source=search)  
[RH - Linha Protheus - GPE - Como fazer transferência de funcionários em Lote](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057503354-RH-Linha-Protheus-GPE-Como-fazer-transfer%C3%AAncia-de-funcion%C3%A1rios-em-Lote?source=search)  
[RH - Linha Protheus - GPE - Tabelas envolvidas na transferência rotina GPEA180](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026535713-RH-Linha-Protheus-GPE-Tabelas-envolvidas-na-transfer%C3%AAncia-rotina-GPEA180)
