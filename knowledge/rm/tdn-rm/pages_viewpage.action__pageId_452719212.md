---
content_hash: 94857a0d623680e12075378f2f91f8fac0051ea262bf08ac5c5ec7960f34ffb4
fetched_at: '2026-06-29T00:10:04.522299+00:00'
page_id: '452719212'
product: rm
source: tdn-rm
title: Modificação de Ocorrências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719212
version: 11
---

Gerar ocorrência modificada na alteração de atitude da ocorrência coletada

 Saiba mais em: [Gerar ocorrência modificada na alteração de atitude da ocorrência no portal](https://tdn.totvs.com/display/public/LRM/TTOATX_DT_Atitude_da_Ocorrencia)

**Modificação de Ocorrências**

---

Este módulo permite que  usuário possa alterar informações como tipo de ocorrência e atitude das ocorrências calculadas dentro do período de apuração. Com essa nova funcionalidade, o usuário não perderá as informações originais da ocorrência calculada pois há uma rastreabilidade após o cálculo da modificação que indica a ocorrência origem da modificação. Será possível realizar os seguintes procedimentos através do cadastro de Modificações de Ocorrências:  
Visualizar as modificações de ocorrência cadastradas na visão padrão. Edição das modificações de ocorrência (inclusão, alteração e exclusão).

**Parâmetros:**  
Chapa do funcionário : Informe a chapa do funcionário que deseja alterar ocorrência Tipo de ocorrência destino: Informe a ocorrência que deverá prevalecer após o recálculo. Caso nenhuma ocorrência seja definida, não haverá alteração quanto ao tipo de ocorrência.

Atitude : Este campo define a atitude da ocorrência. São três tipos de alteração: Pagar, Compensar e Não alterar.  *Observação: Caso ocorra alteração de atitude essa deverá prevalecer após o processo de cálculo.*

Por intervalo: Será considerado o intervalo de datas e horas para efetivar a alteração.

Número de horas : Será considerado o número de horas para cada dia do intervalo.

Justificativa: Insira uma justificativa para alteração. Campo não é obrigatório.

Considera somente interseção com as ocorrências calculadas: Caso selecionar o parâmetro ele irá considerar somente  a interseção ao realizar a modificação. *Observação: Vide maiores informações do parâmetro no subitem Cálculo.*

Tipos de ocorrência origem: Será a ocorrência que terá modificações. Caso não seja informada nenhuma ocorrência todas serão consideradas.

**Cálculo:**  
O cálculo ocorrerá com base nas informações repassadas no cadastro de modificação. O parâmetro "Considera somente interseção com as ocorrências calculadas" irá variar o resultado da alteração conforme sua seleção. O cálculo ser comportará da seguinte maneira:

**Parâmetro Selecionado:**  
-Caso a modificação não faça interseção com nenhuma ocorrência calculada não será criada nenhuma ocorrência calculada modificada.  
-Caso a modificação seja por intervalo, irá buscar diretamente os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.  
-Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência.  
-Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem: Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.  
-Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem: Serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que fazem interseção serão gravadas na tabela de modificação de ocorrência calculada.

**Parâmetro não selecionado:**  
-Caso a modificação não faça interseção com nenhuma ocorrência calculada será criada uma nova ocorrência calculada modificada.  
-Caso a modificação seja por intervalo, irá buscar diretamente os intervalos da ocorrência calculada para validar a interseção com o intervalo da modificação de ocorrência.  
-Caso a modificação seja por número de horas, irá buscar as n primeiras horas das ocorrências calculadas para validar a interseção com o número de horas da modificação de ocorrência .  
-Caso a modificação faça interseção com ocorrências calculadas e não tenha tipos de ocorrência origem: Serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.  
-Caso a modificação faça interseção com ocorrências calculadas e tenha tipos de ocorrência origem: Serão filtradas as ocorrências calculadas com os tipos de ocorrência origem equivalentes. Serão geradas novas ocorrências calculadas com os intervalos que não fazem interseção. Será gerada uma nova ocorrência calculada igual o cadastro da modificação com o intervalo/número de horas de interseção. As ocorrências calculadas que foram geradas serão gravadas na tabela de modificação de ocorrência calculada.  
O usuário também poderá realizar as alterações através  "Automação de Ponto | Movimento | Ocorrências Calculadas | Processos | Gera modificação de ocorrência calculada" possibilitando realizar modificações a partir dos registros de ocorrências calculadas já presentes na tela. Para realizar o rastreamento da ocorrência origem da ocorrência modificada deve selecionar a ocorrência em  Automação de Ponto | Movimento | Ocorrências Calculadas  e em seguida acessar Anexo| Modificação de ocorrência calculada. Caso a ocorrência tenha sido modificada, nesta tela constará o registro de alteração indicando a ocorrência origem.

**Observação****:** Ocorrência de EIJ- Extra de Inter-Jornada ou DSR/DSP -Descanso Semanal Remunerado/ Perdido não são consideradas para o cálculo das ocorrências a serem modificadas.

---

 As informações relacionadas ao cadastro de modificações de ocorrências serão gravadas nas tabelas **AMODIFICAOCORRENCIA** e **AMODIFICAOCORRENCIAORIGEM**.   
Informações relacionadas as modificações de ocorrências calculadas serão gravadas na tabela **AMODIFICAOCORRENCIACALCULADA**.  
O acesso ao menu principal de Modificações de ocorrências é feito através de :  Automação de Ponto | Movimento | Ocorrências | Modificação de Ocorrências     
O acesso ao menu de Modificações de ocorrências poderá ser realizado também pelos seguintes caminhos:  Cadastro de Funcionário | Anexos | Movimento do Ponto | Modificação de Ocorrência , ou   Cadastro de Funcionário | Espelho .NET | Anexos | Modificação de Ocorrência Cadastro de Funcionário | Espelho .NET | Botão de atalho | Modificação de Ocorrência

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

Gestão por Escala - RM Portal
