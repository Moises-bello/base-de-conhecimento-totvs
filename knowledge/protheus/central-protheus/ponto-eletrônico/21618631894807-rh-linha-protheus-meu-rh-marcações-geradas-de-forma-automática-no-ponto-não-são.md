---
article_id: 21618631894807
category: PONTO ELETRÔNICO
content_hash: c1cc66a405f6367fa3a015fcf9889ab06bc43576d94ecb45612abc215e392f2d
fetched_at: '2026-06-28T22:44:36.517947+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - Marcações geradas de forma automática no Ponto,
  não são demonstradas no App Meu RH
type: support-article
updated_at: '2026-06-26T21:31:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21618631894807-RH-Linha-Protheus-Meu-RH-Marca%C3%A7%C3%B5es-geradas-de-forma-autom%C3%A1tica-no-Ponto-n%C3%A3o-s%C3%A3o-demonstradas-no-App-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21618631877143) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Marcações geradas de forma automática no Ponto, não são demonstradas no App Meu RH   
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
No módulo **Ponto Eletrônico, SIGAPON**, temos a possibilidade de configurar o intervalo do almoço, ou as demais marcações do dia, **como automático**, ou seja, o funcionário não precisa realizar a batida manual de almoço, **sendo que o Protheus cadastra automaticamente diante da configuração da Tabela de Horário Padrão.**  
  
Marcações com o campo **P8\_FLAG como A, são Marcações Automáticas** conforme cadastro da Regra de Apontamento, e execução da rotina de **Leitura/Apontamento.**  
   
O espelho de ponto do Meu RH por padrão, assim como a tela de marcações do Meu RH, **mostrarão toda e qualquer marcação que estiver apontada na SP8**, sendo de qual conteúdo, o **campo P8\_FLAG** tiver.  
   
O que será necessário garantir:  
- período de apontamento de todos os registros de marcações na SP8, está igual ao parâmetro de período aberto, ou seja, **campo P8\_PAPONTA = MV\_PONMES**;  
- **campo P8\_APONTA = S** , ou seja, que todas as marcações estão apontadas corretamente via PONM010 ou PONA280 (Integrados) de forma individual ou em lote;  
- **campo P8\_ORDEM** dessas marcações em ordem correta, diante ao período de apontamento;  
- as marcações de intervalo automático não estejam desconsideradas ou deletadas.  
  
No mais, todo e qualquer registro de marcação feita pelo funcionário, gravado na SP8 e estando corretamente apontado, **o Meu RH demonstrará no padrão do Espelho de Ponto e na tela de marcações (*****browser*****) para o funcionário.**  
  
**O parâmetro MV\_GETMAUT**, precisa estar configurado para carregar as marcações de forma automática no Ponto Eletrônico, após o apontamento, seja via rotina **PONM010** - Leitura e Apontamento, **PONA040** ou **PONA280**, Lançamento de Marcações e Integrados, respectivamente.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21620178580759)  
  
Para carregar as Marcações Automáticas nos processos de Leitura, Apontamento e Manutenção das Marcações, deve ser configurado o parâmetro **MV\_GETMAUT com conteúdo S**.  
  
Se após gerar as marcações automáticas para o funcionário, for verificado que existem marcações eletrônicas a serem lidas, **quando for processada a rotina de Leitura/Apontamento**, as marcações automáticas serão substituídas pelas marcações eletrônicas automaticamente.  
  
**Com conteúdo igual a N**, o sistema não carrega as marcações automáticas nos processos de Leitura/Apontamento, e consequentemente, **por conta do App Meu RH ser um espelho do que está já configurado no módulo 16 - SIGAPON**, as marcações não serão demonstradas aos funcionários.  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
