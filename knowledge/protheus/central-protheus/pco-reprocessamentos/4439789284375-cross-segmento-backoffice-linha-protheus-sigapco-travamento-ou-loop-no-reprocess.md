---
article_id: 4439789284375
category: PCO - Reprocessamentos
content_hash: 43bd49a65de438ca75fc4c9833c335d0e0bc6b607a5be41bd0748724ed17a7ad
fetched_at: '2026-06-28T22:37:07.028766+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO: Travamento ou LOOP no
  reprocessamento de Saldo no PCO'
type: support-article
updated_at: '2025-07-01T18:09:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439789284375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Travamento-ou-LOOP-no-reprocessamento-de-Saldo-no-PCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33180380559511) Tempo aproximado para leitura: **00:02:00 min****Dúvida**O que fazer quando o sistema trava ou entra em LOOP no reprocessamento de Saldo no PCO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPCO - Todas as versões]  
  
**Solução**

Verificar pontualmente onde o problema está ocorrendo, para isso precisamos criar pontos de verificação com rotinas simples de acordo com as orientações abaixo:

1.1 Criar um cubo com chave simples   
Conta Orçamentária + Tipo de Saldo)  
Exemplo AKD->AKD\_CO+AKD->AKD\_TPSALD   
  
Status do cubo = 1-Livre p/ Reprocessamento   
  
1.2. Realize um Movimento na tabela AKD através da rotina PCOA050   
Confirme a gravação do Saldo na Tabela AKT   
  
1.3. Ajustar os parâmetros:

MV\_PCOINTE = 1   
MV\_PCOTHRD = 2

**Obs.:** Em relação à quantidade de threads definida pelo parâmetro MV\_PCOTHRD, recomenda-se avaliar a configuração ideal de acordo com a infraestrutura disponível. Esse valor pode chegar até 10, mas deve ser ajustado com o objetivo de obter o melhor ganho de performance possível, evitando sobrecarregar a capacidade de processamento com múltiplas threads em execução simultânea, o que poderia causar o efeito inverso ao desejado.

1.4. Na rotina **PCOA301**  
Na opção perguntas, informar:   
O código do Cubo (simples cadastrado)   
Data do lançamento - período De ... Até (no máximo 2 dias)   
Tipo de Saldo = específico  
Tipo de Saldo Base = O saldo que informou no lançamento  
Voltar para tela inicial clicando em informações e executar.  
  
Se o sistema travar ou entrar em LOOP, verificar como está o compartilhamento das tabelas:  
O reprocessamento utiliza as tabelas AKD AKT AL1 AL2 AL3 AL4 AL5.

As mesmas devem seguir a orientação do documento:

<https://tdn.totvs.com/pages/releaseview.action?pageId=271667086>

Importante testar o cenário com contas orçamentárias novas e com as contas orçamentárias que apresentaram o problema.

Persistindo com as contas antigas, seguir o passo 2.

2.1 Verifique na tabela **AK5** se todas as contas são válidas.

2.2. Verifique se as contas superiores = sintéticas e as inferiores = analíticas 

Ajustar caso haja inconsistências e refazer o teste.

Persistindo o problema em ambiente atualizado de acordo com o portal, entrar em contato com o suporte com os passos para reprodução do problema, ou com situação pontual levantada.
