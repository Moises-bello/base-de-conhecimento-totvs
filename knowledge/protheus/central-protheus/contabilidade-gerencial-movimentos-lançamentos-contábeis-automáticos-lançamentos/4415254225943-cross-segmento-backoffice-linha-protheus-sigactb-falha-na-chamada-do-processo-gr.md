---
article_id: 4415254225943
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: b06d3f39adc282d91a8cb8f42c01d0958048a224edb96f763882b1da6418f962
fetched_at: '2026-06-28T22:40:32.515352+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Falha na chamada do
  processo - Gravação de Saldos - Stores Procedure CTB153_6
type: support-article
updated_at: '2021-12-07T19:37:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415254225943-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Falha-na-chamada-do-processo-Grava%C3%A7%C3%A3o-de-Saldos-Stores-Procedure-CTB153-6
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**Ao realizar uma operação contábil que exige a atualização dos saldos contábeis (Via lançamento de integração ou lançamento manual ou apuração de resultado ou efetivação de lançamento) o sistema retorna o help: Falha na chamada do processo - Gravação de Saldos - Stores Procedure CTB153\_6  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1.Realize as desinstalação e a Diretamente no servidor  instalação das **[Procedure](https://tdn.totvs.com/pages/viewpage.action?pageId=382557083)**  
  
Em modo exclusivo:  
1º Reinicie o serviço.  
2º Desinstale as procedures existente em seu ambiente.  
3º Verifique se o sistema desinstalou do configurador.  
4º Verifique se o sistema [desinstalou do Banco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search) antes de instalar novamente.  
5º Copie as procedures atualizadas na pasta system.  
6º Instale as procedures .  
7º Reinicie o serviço.  
  
2. Violação de Chave única da tabela :Verificar procedimento descrito no link: [Erro ao atualizar os saldos (Unique constraint)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000737728-MP-SIGACTB-Erro-ao-atualizar-os-saldos-Unique-constraint-)  
Obs: pode ser apresentado em Tela ou no Trace  
3. Estouro de Campo  
Em caso de Estouro de Campo, deve-se verificar qual é o campo e avaliar a alteração da estrutura de todas as tabelas de saldos para o maior tamanho possível ,sugerimos realizar a  [ALTERAÇÃO DO TAMANHO DAS ENTIDADES CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015543251-MP-SIGACTB-ALTERA%C3%87%C3%83O-DO-TAMANHO-DAS-ENTIDADES-CONT%C3%81BEIS?source=search) , [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) e [Tamanho do campo código das entidades contábeis Adicionais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401031-MP-SIGACTB-Alterar-o-tamanho-do-campo-c%C3%B3digo-das-entidades-cont%C3%A1beis-adicionais?source=search) estão corretos.

4. Verifique se o seu ambiente esta atualizado com o último pacote disponível do Módulo Contabilidade Gerencial:

**[Pacotes de Atualização - Contabilidade](https://tdn.totvs.com/pages/releaseview.action?pageId=334342777)**
