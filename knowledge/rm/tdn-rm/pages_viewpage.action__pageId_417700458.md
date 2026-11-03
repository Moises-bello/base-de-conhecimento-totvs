---
content_hash: 4ec95daf01c117aa4c20fae9954b79c38062a4493d2be2a417801c6005278270
fetched_at: '2026-06-29T00:09:12.701312+00:00'
page_id: '417700458'
product: rm
source: tdn-rm
title: Movimentação de Leito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700458
version: 1
---

**Movimentação de Leito**   
             Agora no nosso aplicativo temos um processo chamado Movimentação de Leitos. O TOTVS Controle de Infecção Hospitalar terá uma melhor integração com o sistema de Gestão Hospitalar mostrando e identificando através da tela do aplicativo e também em relatórios BI  quais foram os tipos de passagem do paciente pelo hospital, identificando a sua unidade Clínica com as suas respectivas movimentações e também seus procedimentos. Mais como  funciona esta nova importação?   
             Antes de realizar a importação da movimentação terá que ser definido o "DE-PARA"  entre o sistema de origem e Controle de Infecção Hospitalar na tela de cadastro / Unidade Clínica. Lembrando que se na internação do paciente não estiver uma unidade clínica cadastrada o sistema ira criar uma "UND. TEMPORÁRIA" para uma melhor validação do cliente depois de feita a importação da movimentação.  
            Após ser definido o código do leito tem que ser realizada a importação de dados que também poderá ser feita através de TXT ou VIEW. O Processo de movimentação de leito se encontra na tela de Menu / Utilitários / Importação / Ajuste Movimentação. Lembrando que para esta importação acontecer será necessário ter a internação do paciente para o nosso aplicativo. Depois de importar a movimentação, o cliente entrara na nova tela de paciente do aplicativo. Na tela agora não existe mais a aba "área crítica" e sim as internações com suas respectivas movimentações e o melhor com a data e hora da movimentação do paciente.   
            Como pode ser visto na tela abaixo existe a data e a hora da entrada e saída da movimentação, se não existir a data de saída o importador, ira fechar automaticamente a data de saída de acordo com a data de entrada da próxima movimentação fez.  
            Foi uma grande novidade para esta versão no TOTVS Controle de Infecção Hospitalar, lembrando que se o usuário não quiser realizar ou não tiver no seu sistema de origem este tipo de informação não tem problema, pois pode ser utilizada ou não sem que interfira nos processos já existentes.  
Para maiores informações, [Clique aqui](http://totvsconnect.blogspot.com/2010/10/como-fazer-totvs-movimentacao-de-leitos)**.**
