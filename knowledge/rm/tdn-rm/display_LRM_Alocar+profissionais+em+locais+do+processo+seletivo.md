---
content_hash: 3e214975cf3504f6aafdff2ca9105eb7abb2ae4a026a9baa94e29103cfd3dab5
fetched_at: '2026-06-29T00:09:29.823428+00:00'
page_id: '425458296'
product: rm
source: tdn-rm
title: Alocar profissionais em locais do processo seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Alocar+profissionais+em+locais+do+processo+seletivo
version: 2
---

Através dos profissionais e locais previamente cadastrados no sistema, será possível que este processo aloque todos os profissionais nos locais necessários levando-se em conta seus perfis.

Utilizando o processo: Para executar este processo não será necessário o preenchimento de quaisquer informações, ele apenas exibirá o processo seletivo para o qual o mesmo será executado.

O processo irá verificar se todos os profissionais cadastrados são suficientes para preencher as exigências de todos os locais. Caso falte algum tipo de profissional para algum local o processo irá notificar no final da execução.   
 Após a execução do processo será exibido um Log. notificando o resultado do processamento. O log. do processo também exibirá ao seu final um alerta para alocação de profissionais em locais provas sem candidatos. Será mostrada uma lista com a relação de salas de provas que não possuírem candidatos alocados em que forem alocados profissionais.

Caso haja necessidade de cadastrar novos profissionais, basta executar o processo novamente para que o mesmo aloque-os nos locais restantes. Este processo poderá ser executado várias vezes, pois os profissionais que já foram alocados não sofrerão alterações, apenas os locais que ainda precisarem de profissionais terá os mesmos alocados.

**Pré - requisitos do processo**:  
 **a)** Ter cadastrado previamente os profissionais através da tabela auxiliar Profissional.  
 **b)** Ter cadastrado previamente os locais do processo seletivo através do serviço Local de Processo Seletivo.
